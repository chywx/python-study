from selenium import webdriver

import time

from selenium.webdriver.common.by import By


def a():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    time.sleep(3)
    driver.quit()


def b():
    # 我们需要操作的浏览器，这里使用的是谷歌浏览器，也可以是IE、Firefox
    driver = webdriver.Chrome()
    # driver.fullscreen_window()
    # 访问百度首页
    driver.get('https://www.baidu.com')
    # 停3秒钟
    time.sleep(3)
    # 百度输入框的id为kw，我们需要在输入框中输入Selenium，用send_keys进行输入
    driver.find_element(By.ID, "kw").send_keys("Selenium")
    time.sleep(3)
    # 百度搜索框按钮id叫su，找到后调用click函数模拟点击操作
    # 和click有相同效果的是submit(),都可以用来点击按钮，submit主要是用于提交表单
    driver.find_element(By.ID, "su").click()
    time.sleep(3)
    # 退出并关闭窗口的每一个相关的驱动程序
    driver.quit()


if __name__ == '__main__':
    # a()
    b()
