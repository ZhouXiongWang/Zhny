#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 15:57
# @Author  : Zxw


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
options = webdriver.ChromeOptions()
CHROMEDRIVER_PATH= "D:\\WorkSpace\\Zany\\chromedriver.exe"
service = ChromeService(service=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
driver.get(f"https://www.baidu.com")
driver.get_screenshot_as_png()
time.sleep(5)
