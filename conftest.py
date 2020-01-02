# coding:utf-8
"""
author:zhouxuan
@project--file : erp2 -->conftest.py
2019/12/31 9:57
@Desc:
"""
from selenium import webdriver
from conf.config import *
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time
@pytest.fixture()
def login(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(SYS_URL)
    driver.find_element(value='username').send_keys('testuser@tongtool.com')
    driver.find_element(value='password').send_keys('testuser',Keys.ENTER)
    time.sleep(6)
    value= request.param
    target_element=driver.find_element_by_link_text(value[0])
    ActionChains(driver).move_to_element(target_element).perform()
    driver.find_element_by_link_text(value[1]).click()
    yield driver
    # driver.quit()

