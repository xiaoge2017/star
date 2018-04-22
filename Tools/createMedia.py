# -*- coding:utf-8 -*-
'''
创建media下的几个空文件夹
'''

import os

my_file_ROOT = 'D:/star'
my_file_media = 'media'
add_Media = my_file_ROOT + '/' + my_file_media
my_file_media_dir = ['file','files','img','imgs','soft','pic_folder']

def mkdir(add_Media):
    for i in my_file_media_dir:
        add_dir = add_Media + '/' + i
        # print(add_dir,os.path.exists(add_dir))
        if os.path.exists(add_dir)==False:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(add_dir)  # 创建文件时如果路径不存在会创建这个路径
            print(add_dir+'创建好了')
        else:
            print ('没有这样的文件路径: %s ' % add_dir)

mkdir(add_Media)