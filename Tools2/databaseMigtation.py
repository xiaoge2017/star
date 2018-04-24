#-*- coding:utf-8 -*-
import os
def DatabaseMigtationOut(my_file_ROOT,operate4):
    os.chdir(my_file_ROOT)#切换工作目录
    os.system(operate4)

def DatabaseMigtationIn(my_file_ROOT,operate5):
    os.chdir(my_file_ROOT)#切换工作目录
    os.system(operate5)