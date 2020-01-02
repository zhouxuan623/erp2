# coding:utf-8
"""
author:zhouxuan
@project--file : erp2 -->test_category.py
2019/12/31 10:35
@Desc:分类管理
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.parseconfig import parseConfig
from common.s_packaging import packaging
from conf.config import PRODUCT_DIR,COMMON_DIR
import os
class Test_Category():
    @pytest.mark.parametrize('login',[('商品管理','分类管理')],indirect=True)
    def test_add(self,login):
        driver=login
        product=packaging('test_cateorgy',PRODUCT_DIR)
        product.click_obj(driver,'添加分类')
        product.write_obj(driver,'分类名称','通信产品')
        product.write_obj(driver,'显示顺序',1)
        product.write_obj(driver,'中文报关名称','小米手机')
        product.write_obj(driver,'英文报关名称','mi9max')
        product.click_obj(driver,'保存(新增)')
        success=packaging('common',COMMON_DIR)
        success.wait_element_appear(driver,'成功提示')


if __name__ == '__main__':
    pytest.main(['-s','test_category.py'])

