#-*- coding:utf-8 -*-

import xadmin
from file_db.models import FILE

class File(object):
    list_display = ('id','file','name')
xadmin.site.register(FILE,File)