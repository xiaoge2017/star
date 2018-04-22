#-*- coding:utf-8 -*-

import xadmin
from pro_db.models import a,b,c,staff,soft
from pro_db.models import info as xinxi
from xadmin import views

# ------------可以定制化选主题 S--------------
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

# class UserProfileAdmin(UserAdmin):
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()
# from django.db.models import UserProfile, EmailVerifyRecord, Banner
# class UserProfileAdmin(object):
#     pass
# xadmin.site.register(UserProfile, UserProfileAdmin)

# 基本的修改
class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True  #

# 针对全局的
class GlobalSettings(object):
    site_title = "项目管理后台"  # 系统名称
    site_footer = "star之星"      # 底部版权栏
    menu_style = "accordion"     # 将菜单栏收起来

# 注册，注意一个是BaseAdminView，一个是CommAdminView
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

# ------------可以定制化选主题 E--------------

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


class SOFT(object):
    list_display = ('id', 'name', 'version', 'img','use','downFile')
xadmin.site.register(soft, SOFT)

class XINXI(object):
    list_display = ('id', 'name', 'pwd', 'save')
xadmin.site.register(xinxi,XINXI)