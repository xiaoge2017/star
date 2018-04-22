#-*- coding:utf-8 -*-

import xadmin
from pro_db.models import a,b,c,info,staff,soft

class A(object):
    list_display = ('id','name','address','img','partner','timeS','timeE','brief','tech','show','SVN','Git')
xadmin.site.register(a,A)

class B(object):
    list_display = ('id','name','address','img','partner','timeS','timeE','brief','tech','show','SVN','Git')
xadmin.site.register(b,B)

class C(object):
    list_display = ('id','name','address','img','partner','timeS','timeE','brief','tech','show','SVN','Git')
xadmin.site.register(c,C)

class STAFF(object):
     list_display = ('id', 'name', 'portrait', 'QQ', 'blog', 'job', 'adept', 'other')
xadmin.site.register(staff,STAFF)


class INFO(object):
    list_display = ('id', 'name', 'pwd', 'save')
xadmin.site.register(info,INFO)