#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/12 16:24
# @Author  : Zxw
import pytest

from BaseDriver.Base_Page import BasePage
from Page.BrowserClient.PortalMenu.PirtalMenu import PortalMenu


class ProtalHome(BasePage):

    def __init__(self):
        self.do_getUrl('http://58.49.21.120:9711/xplatf/#/login')

    def LoginPage(self):
        pass

    def RegisterPage(self):
        pass

    def AppDownloadPage(self):
        pass

    def AboutUsPage(self):
        pass

    def EnergyInformationPage(self):
        pass

    def TypicalCasePage(self):
        pass

    def SolutionPage(self):
        pass


    def HomePage(self, args):
        self.do_clickElement(args['PortalPage']['HomePageElement'])

        from Page.BrowserClient.PortalMenu.HomePage.HomePage import HomePage
        return HomePage(self.driver)
