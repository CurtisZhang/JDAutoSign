# JDAutoSign
适用于 JD 员工，可实现内网 ERP 定时打卡，请勿违规使用。
只是个熟悉 Selenium 的实操，欢迎指正～
详细介绍：http://www.curtiswho.com/archives/14/
个人 Blog： http://www.curtiswho.com 

## 原理
主体基于 Python 下的 Selenium 库，通过 `find_element` 方法找到相关元素实现自动登录打卡流程。由于采用 Selenium，因此不存在被反作弊发现的可能。其中 WebDriver 选择 Chromedriver，GUI 界面利用 tkinter 实现（丑，建议各位别用）。


## 环境
如果不太会配环境，我封装了一份执行文件，只需要从 [npm 镜像][1] 下载对应版本的 ChromeDriver 放到同目录下即可，测试版本采用 `86.0.4240` 版本；
如果想直接跑 py，那么所需环境如下：
1. Python 3.6.5；
2. 所需的库：
   + Selenium
   + APSchedule
   + tkinter
   + time / datetime
3. WebDriver如上，可自行选择；


## DEMO
![界面][2]
一个签到脚本就不写使用说明了，这边注意三点即可：
1. 打卡时间必须按照给定格式填写`2020-12-12 08:50：05`；
2. 点击签到后最小化窗口（不要关闭主界面），需要保留线程进行签到；
3. ERP账号不需要填写邮箱后缀；

  [1]: https://npm.taobao.org/mirrors/chromedriver/
  [2]: http://www.curtiswho.com/usr/uploads/2020/12/3639982690.png
