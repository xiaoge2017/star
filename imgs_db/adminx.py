#-*- coding:utf-8 -*-

import xadmin


from imgs_db.models import Imgs,Imgs_name



class test_img_up(object):
    list_display = ('id','name')
xadmin.site.register(Imgs_name, test_img_up)

class img_up(object):
    list_display = ['id','img','single']
    filter_horizontal = ['imgs',]
xadmin.site.register(Imgs, img_up)



