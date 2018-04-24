#-*- coding:utf-8 -*-
'''
变量设置
'''
import os
# initAPP
my_file_ROOT = os.path.dirname(os.getcwd())#返回到当前目录的上一级star
operate0 = 'python manage.py migrate --fake-initial'
operate1 = 'python manage.py makemigrations'
operate2 = 'python manage.py migrate'
operate3 = 'python manage.py createsuperuser'
operate4 = 'manage.py createsuperuser'

#createMedia & delMedia
my_file_media = 'media'
add_Media = my_file_ROOT + '/' + my_file_media
my_file_media_dir = ['file','files','img','imgs','soft','pic_folder']
del_Media = my_file_ROOT + '/' + my_file_media

#createDatabase & delDatabase
db_host = '127.0.0.1'
db_user = 'root1234'
db_pw = 'root1234'
db_name = 'star'

'''
以下为操作
'''
from Tools2 import delMedia
delMedia.DeleteMedia(del_Media)
print ('删除完了上传的图片和文件！')

from Tools2 import createMedia
createMedia.mkdir(add_Media,my_file_media_dir)
print(my_file_media+'创建完成！')

from Tools2 import delDatabase
delDatabase.DelDatabase(db_host,db_user,db_pw,db_name)
print ('删除完了' + db_name + '数据库!')

from Tools2 import createDatabase
createDatabase.AddDatabase(db_host, db_user, db_pw,db_name)
print ('创建完了' + db_name + '数据库!')

from Tools2 import initApp
initApp.INITAPP(my_file_ROOT,operate0,operate1,operate2)
print('第一步初始化完成，接下来手动创建超级管理员并设置密码！')

