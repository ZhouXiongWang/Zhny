#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/12 16:42
# @Author  : Zxw

from Page.BrowserClient.PortalHome import ProtalHome


class Test_Pirtal:

    def setup_class(self):
        self.index = ProtalHome()
        pass

    def teardown_class(self):
        pass

    # # @pytest.mark.parametrize('args',BasePage().read_yaml('Data.yaml'))
    # def test_DemandReporting(self):
    #     """
    #     需求提报测试用例
    #     :return:
    #     """
    #     self.index.GetZhnyPage().HomePage().PartnersJoin()

    def test_DemandReporting(self):
        """
        需求提报测试用例
        :return:
        """
        self.index.GetZhnyPage().HomePage().PartnersJoin()