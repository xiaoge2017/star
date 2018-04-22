# # ------------可以定制化选主题 S--------------
# import xadmin
# from xadmin import views
# from xadmin.plugins.auth import UserAdmin
# from xadmin.layout import Fieldset, Main, Side, Row
# from django.utils.translation import ugettext as _
#
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
#
# # 基本的修改
# class BaseSetting(object):
#     enable_themes = True   # 打开主题功能
#     use_bootswatch = True  #
#
# # 针对全局的
# class GlobalSettings(object):
#     site_title = "慕学后台管理系统"  # 系统名称
#     site_footer = "慕学在线网"      # 底部版权栏
#     menu_style = "accordion"     # 将菜单栏收起来
#
# # 注册，注意一个是BaseAdminView，一个是CommAdminView
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)
#
# # ------------可以定制化选主题 E--------------
