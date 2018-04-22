#-*- coding:utf-8 -*-
#-*- coding:utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from files_db.models import Files,Files_name

class test_file_up(object):
    list_display = ('id','name','files')
xadmin.site.register(Files_name, test_file_up)

class file_up(object):
    list_display = ['id','file']
    # filter_horizontal = ['imgs',]
xadmin.site.register(Files, file_up)


