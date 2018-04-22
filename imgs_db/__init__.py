#-*- coding:utf-8 -*-
import pymysql
pymysql.install_as_MySQLdb()

from django.apps import AppConfig
import os

default_app_config='imgs_db.ImgsDbConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class ImgsDbConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '多图片数据库'
