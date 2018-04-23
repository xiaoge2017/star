# -*- coding:utf-8 -*-
'''
在每个APP的migrations文件夹下，保留__init__.py文件，删除其他文件
'''

import os
import os.path

my_file_ROOT = 'C:/Users/wyc/Desktop/star'
my_file_APP = ['file_db','files_db','img_db','imgs_db','pro_db','xadmin']
my_file_migartions = 'migrations'
my_file_init = '__init__.py'
undel_file_list = [r'\__init__.py',]

def DeleteFiles(path,fileList):
    for parent,dirnames,filenames in os.walk(path):

        FullPathList = []
        DestPathList = []

        for x in fileList:
            DestPath = path + x
            DestPathList.append(DestPath)


        for filename in filenames:                   
            FullPath = os.path.join(parent,filename)
            FullPathList.append(FullPath)


        for xlist in FullPathList:
            if xlist not in DestPathList:
                os.remove(xlist)


def DelFiles(my_file_APP,my_file_migartions,undel_file_list):
    for i in my_file_APP:
        del_ROOT = my_file_ROOT + '/' + i + '/' + my_file_migartions
        DeleteFiles(del_ROOT, undel_file_list)

DelFiles(my_file_APP,my_file_migartions,undel_file_list)
print ('删除完了初始化的文件！')
