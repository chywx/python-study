from selenium import webdriver

import time


def a():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    a()