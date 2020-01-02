# coding:utf-8
"""
author:zhouxuan
@project--file : erp2 -->config.py
2019/12/31 9:57
@Desc:
"""
import os
SYS_URL="http://10.0.0.96"

ROOT_DIR=os.path.dirname(os.path.dirname(__file__))  #根目录

CONFIG_DIR = os.path.join(ROOT_DIR,'conf','config.py') #配置文件引用路径

PRODUCT_DIR=os.path.join(ROOT_DIR,'product','product.ini')
COMMON_DIR = os.path.join(ROOT_DIR,'conf','config.ini')
