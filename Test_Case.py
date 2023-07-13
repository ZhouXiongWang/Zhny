import os

import pytest
import yaml

from BaseDriver.Base_Page import BasePage


# def read_yaml( Yaml_file):
#     with open(os.path.dirname(os.path.dirname(__file__)) + f'/Zhny/Datas/{Yaml_file}', "r", encoding="utf-8") as fp:
#         Value = yaml.safe_load(fp)
#     return Value
#
# print(read_yaml('Data.yaml'))
#
# a={'accout': 'guzhen', 'password': 'Zhny@2023', 'case1': [{'id': 1, 'pid': 1}, {'id': 2, 'pid': 2}], 'MenuHome': '(By.XPATH,\'//*[@id="app"]/div/div[1]/div[3]/ul/li[1]/span\')'}
# print(a['accout'])
def read_yaml(Yaml_file):
    with open(os.path.dirname(os.path.dirname(__file__)) + f'/Zhny//Datas//{Yaml_file}', "r", encoding="utf-8") as fp:
        Value = yaml.safe_load(fp)
    return Value

@pytest.mark.parametrize('f', read_yaml(f'Data.yaml'))
def  aaa(f):
    print()

__name__==