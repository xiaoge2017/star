# -*- coding:utf-8 -*-
'''
删除media下的文件
'''

import os

def DeleteMedia(del_Media):
    for i in os.listdir(del_Media):
        del_dir = None
        del_dirFile = os.path.join(del_Media,i)
        if os.path.isfile(del_dirFile):
            #如果是文件则删除
            print(del_dirFile)
            os.remove(del_dirFile)
        else:
            #不是文件只能是目录，就遍历后再删除
            del_dir = del_dirFile
            for j in os.listdir(del_dir):
                del_dir_files = os.path.join(del_dir, j)
                print(del_dir_files)
                os.remove(del_dir_files)
