#-*- coding:utf-8 -*-

import xadmin
from img_db.models import IMG

class Img(object):
    list_display = ('id','img','name')
xadmin.site.register(IMG,Img)
