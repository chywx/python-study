from selenium import webdriver

import time


def a():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com/')
    time.sleep(3)
    b.quit()


if __name__ == '__main__':
    a()