#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 9:40
# @Author  : Zxw
import os
import time

import allure
import yaml
import numpy as numpy
from PIL import Image
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType, get_browser_version_from_os
from Logeer.log_util import logger
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromiumService


class BasePage:
    _screenshot_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    _File_Path = os.path.dirname(os.path.dirname(__file__)) + f"/screenshots/" + _screenshot_time + '.png'
    _cache = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/cache'

    def __init__(self, driver: WebDriver = None, headless=False, net=True):
        logger.info(f"当前页面的driver对象:{driver}")

        if driver is None:
            option = webdriver.ChromeOptions()
            # 开启沙盒模式
            option.add_argument('--no-sandbox')
            option.add_argument('--disable-dev-shm-usage')
            # 放弃等待图片、样式、子帧的加载。
            option.page_load_strategy = 'eager'
            # 忽略安全证书问题
            option.add_argument(f"--test-type --ignore-certificate-errors")
            if headless:
                # 无头模式开启开关
                option.add_argument('headless')
                logger.info(f"当前开启无头模式")
                # 设置无头浏览器下指定分辨率
                option.add_argument('window-size=1920,1080')
            if net:
                # 有网路的情况下可使用下列webdriver-manager自动下载webdriver驱动
                # 获取当前谷歌浏览器版本
                BrowserVersion = get_browser_version_from_os("google-chrome")
                logger.info(f"正在下载webdriver驱动,当前浏览器版本为：{BrowserVersion}")
                self.driver = webdriver.Chrome(service=ChromiumService(
                    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, path=os.path.dirname(os.path.dirname(__file__))
                                                                              + '/Webdrivers').install(),
                    options=option))
            elif not net:
                # webdriver驱动地址
                driver_path = os.path.dirname(os.path.dirname(__file__)) + '/Webdrivers'
                logger.info(f"当前使用本地驱动,驱动地址为{driver_path}")
                service_path = ChromeService(executable_path=driver_path)
                self.driver = webdriver.Chrome(options=option, service=service_path)
            # 设置全局的隐式等待
            # self.driver.implicitly_wait(10)
            logger.info(f"当前隐式等待10s")
            # 设置窗口最大化
            self.driver.maximize_window()
            logger.info(f"当前窗口最大化")
        else:
            self.driver = driver
            logger.info("当前驱动已存在")

    def do_waitGetElement(self, by: By, location: str):

        """
        该方法为寻找元素
        可传元组类型或普通定位方式
        例： ele=(By.Xpath,"//div[@class='123']")
            self.find_ele(*ele)
        :param by:定位方式
        :param location:元素
        :return:元素
        """
        try:
            # 使用WebDriverWait和expected_conditions来设置一个超时时间和一个条件
            # visibility_of_element_located表示等待元素可见
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, location)))
        except (NoSuchElementException, TimeoutException) as e:
            logger.error(f"当前元素未找到，定位方式为{by},元素为:{location}")
            raise Exception(
                '[{}]寻找元素异常:定位方式为{},元素为:{},查看元素定位是否正确'.format(os.path.basename(__file__), by,
                                                                                      location)) from e

    def do_clickElement(self, by: By, location: str):
        """
        进行点击元素操作，可传元组
        :param by: 定位方式
        :param location: 元素
        :return:
        """
        self.do_waitGetElement(by, location).click()

    def do_sendKey(self, by: By, location: str, key):
        """
        在输入框中输入值，可传元组
        :param by: 定位方式
        :param location: 元素
        :param key:需要输入的值
        :return:
        """
        element = self.do_waitGetElement(by, location)
        element.click()
        logger.info(f"正在输入{key}")
        element.send_keys(key)

    def do_sendkeyAndClaer(self, by: By, location: str, key: str):
        """
        现清除输入框中的值，在进行输入操作，可传入元组
        :param by: 定位方式
        :param location: 元素
        :param key:需要输入的值
        :return:
        """
        element = self.do_waitGetElement(by, location)
        element.click()
        element.clear()
        logger.info(f"正在输入{key}")
        element.send_keys(key)

    def do_javaScript(self, script, *args):
        """
        执行JavaScript脚本
        :param script:被执行的JavaScript脚本
        :return:
        """
        self.driver.execute_script(script, args)

    def do_clear(self, by: By, location: str):
        """
        清除输入框,可传入元组
        :param by: 定位方式
        :param location: 元素
        :return:
       """
        element = self.do_waitGetElement(by, location)
        element.clear()

    def do_movePage(self, x, y):
        """
        移动页面值指定X.Y坐标
        :param x:
        :param y:
        :return:
        """
        self.do_javaScript('window.scrollTo(%s,%s)' % (x, y))
        logger.info(f"页面移动值{x}，{y}")

    def actions(self):
        """
        实例化鼠标Actions实例
        :return:
        """
        actions = webdriver.ActionChains(self.driver)
        logger.info(f"鼠标实例化成功")
        return actions

    def do_switchIframe(self, by, location):
        """
        切换iframe,frame框架
        :return:
        """
        self.driver.switch_to.frame(self.do_waitGetElement(by, location))

    def do_switchToHeadle(self, Headle=None):
        """
        切换句柄,將驅動跳轉至最新頁面,
        不傳headle默認跳轉至最新句柄，传入Headle则调准值指定句柄中
        :return:
        """
        if Headle is None:
            headle_list = self.driver.window_handles
            self.driver.switch_to.window(headle_list[-1])
        else:
            try:
                self.driver.switch_to.window(Headle)
            except Exception as e:
                logger.error(f"切换句柄失败，查看传入句柄是否正确{Headle}")
                raise e

    def do_closePageAndSwitchToHeadle(self):
        """
        关闭其它页面，并切换句柄
        :return:
        """
        headle_list = self.driver.window_handles
        headle = self.driver.current_window_handle
        # 判断页面数量
        while len(headle_list) >= 2:
            # 当当前页面句柄不等于第一个页面句柄时，执行关闭第一句柄操作，直到当前页面句柄等于第一个句柄时结束
            if headle != headle_list[0]:
                self.driver.switch_to.window((headle_list[0]))
                self.driver.close()
                headle_list = self.driver.window_handles
            if headle == headle_list[0]:
                logger.info(f"当前句柄等于列表中第一个句柄，循环关闭页面操作结束")
                break
        headle_list = self.driver.window_handles
        self.driver.switch_to.window(headle_list[-1])

    def do_screenshot(self):
        self.driver.save_screenshot(self._File_Path)
        allure.attach.file(source=self._File_Path, name=f'{self._screenshot_time}.png')
        logger.info(f"成功截图，截图名称:{self._screenshot_time}.png")

    def do_screenshotForPage(self):
        """
        将整个页面截图凭借在一起
        :return:
        """
        window_height = self.driver.execute_script("return window.screen.height")  # 屏幕高度
        page_height = self.driver.execute_script("return document.documentElement.scrollHeight")  # 页面高度
        wp = page_height // window_height
        if wp == '0':
            self.driver.save_screenshot(self._File_Path)
        else:
            for i in range(wp + 1):
                self.driver.execute_script("window.scrollBy(0,{})".format(i * window_height))
                time.sleep(0.5)
                self.driver.save_screenshot(r'{}\{}.png'.format(self._cache, i))
            target_img = os.listdir(self._cache)
            base_mat = numpy.atleast_2d(Image.open(os.path.join(self._cache, target_img[0])))
            for i in target_img[1:]:
                mat = numpy.atleast_2d(Image.open(os.path.join(self._cache, i)))  # 打开截图并转为二维矩阵
                base_mat = numpy.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
            Image.fromarray(base_mat).save(os.path.join(self._File_Path))
        allure.attach.file(source=self._File_Path, name=f'{self._screenshot_time}.png')

    def do_pageSizeScreenshot(self, window_location_left, window_location_upper, window_location_right,
                              window_location_lower):
        """
              进行屏幕截图且获取指定大小的截图
            :param window_location_left: 截图左
            :param window_location_upper: 截图高
            :param window_location_right: 截图右
            :param window_location_lower: 截图低
            :return:
            """
        self.driver.save_screenshot(self._File_Path)
        # 获取selenium截图
        im = Image.open(self._File_Path)
        # 对截图按像素点裁剪
        region = im.crop(
            (window_location_left, window_location_upper, window_location_right, window_location_lower))
        # 输出裁剪后图片
        region.save(self._File_Path)
        allure.attach.file(source=self._File_Path, name=f'{self._screenshot_time}.png')

    def do_forward(self):
        """
        浏览器前进操作
        :return:
        """
        self.driver.forward()

    def do_back(self):
        """
        浏览器后退操作
        :return:
        """
        self.driver.back()

    def do_refresh(self):
        """
        浏览器刷新操作
        :return:
        """
        self.driver.refresh()

    def do_getUrl(self, url):
        """
        打开url页面
        :param url: URl地址
        :return:
        """
        self.driver.get(url)

    def do_quit(self):
        """
        关闭浏览器及驱动
        :return:
        """
        self.driver.quit()

    # 关闭当前页面
    def do_close(self):
        """
        关闭当前浏览器页面
        :return:
        """
        self.driver.close()

    def read_yaml(self, Yaml_file):
        with open(os.path.dirname(os.path.dirname(__file__)) + f'/Datas//{Yaml_file}', "r", encoding="utf-8") as fp:
            Value = yaml.safe_load(fp)
        return Value
