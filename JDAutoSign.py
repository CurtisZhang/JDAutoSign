# -*- coding: utf-8 -*-
"""
Created on 2020-11-30
@author: Curtis
@site: http://www.curtiswho.com
"""

import tkinter as tk
import tkinter.messagebox
import pickle
import time
import sys
import os
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#相对路径-->绝对路径
def resourcePath(relativePath):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relativePath)

#窗口
window=tk.Tk()
window.title('京东 AutoSign')
window.geometry('400x300')
#画布放置图片
canvas = tk.Canvas(window, height = 300, width = 400)
imagefile = tk.PhotoImage(file = resourcePath('JD.png'))
image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
canvas.pack(side = 'top')
#LABEL:ERP/PWD
tk.Label(window, text = 'ERP:').place(x = 80, y = 20)
tk.Label(window, text = '密码:').place(x = 80, y = 60)
tk.Label(window, text = '时间:').place(x = 80, y = 100)
#ERP输入框
var_erp=tk.StringVar()
entry_erp=tk.Entry(window, textvariable = var_erp)
entry_erp.place(x = 140, y = 20)
#PWD输入框
var_pwd=tk.StringVar()
entry_pwd=tk.Entry(window, textvariable = var_pwd, show = '*')
entry_pwd.place(x = 140, y = 60)
#TIME输入框
var_time=tk.StringVar()
entry_time=tk.Entry(window, textvariable = var_time)
entry_time.place(x = 140, y = 100)
entry_time.insert(0, '2020-12-12 08:50:50')
 
#签到函数
def sign():
    #输入框获取用户名密码
    erp=var_erp.get()
    pwd=var_pwd.get()
    time=var_time.get()
    #新建本地Pickle数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info, usr_file)
    if erp == '' or pwd == '' or time == '':
        tk.messagebox.showerror(message = 'ERP or PWD为空!')
    #ERP、PWD完整则开始签到
    else:
        tk.messagebox.showinfo(message = '自动签到正在后台运行中，请勿关闭主程序窗口！')
        #signSelenium(erp,pwd)
        sched = BackgroundScheduler()
        sched.add_job(signSelenium, 'date', run_date = time, args = [erp, pwd])
        sched.start()

#Sign函数
def signSelenium(erp, pwd):
    driver = webdriver.Chrome()
    driver.get("http://erp.jd.com")
    #driver.minimize_windows()

    try:
        #/html/body/div/div[1]/div/div[1]/form/div[1]/label/div/

        #Find Login Module
        driver.find_element_by_xpath("//*[@id='username']").send_keys(erp)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        
        #Imitate Click Login Button
        driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/form/div[4]/input").click()
        time.sleep(2)

        #Imitate Sign Button
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/nav/div[1]/div[2]').click()
        time.sleep(2)
        
        #print("Task Succeed!")
        tk.messagebox.showinfo(message = '自动签到成功！')
        return

    except:
        #print("Task Failed!")
        tk.messagebox.showerror(message = '自动签到失败！')
        return

    driver.quit

#退出的函数
def quit():
    window.destroy()


#登录按钮
bt_login=tk.Button(window, text = '签到', command = sign)
bt_login.place(x = 100, y = 140)
bt_logquit=tk.Button(window, text = '退出', command = quit)
bt_logquit.place(x = 240, y = 140)
#主循环
window.mainloop()