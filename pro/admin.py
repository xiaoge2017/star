from django.contrib import admin
from pro.models import a,b,c,staff,soft


#Blog模型的管理器
# class AuthorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(a, AuthorAdmin)
# class MyAdminSite(admin.AdminSite):
#     site_header = '好医生运维资源管理系统'  # 此处设置页面显示标题
#     site_title = '好医生运维'  # 此处设置页面头部标题
#
# admin.site.register(a, ProAAdmin)
# admin_site = MyAdminSite(name='management')

class ProAAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'address', 'img','colored_status','timeS','timeE','brief','tech','show','SVN','Git','imgs','file')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id','name','partner','timeS','timeE','SVN','Git',)
    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']
    # # fk_fields 设置显示外键字段
    # fk_fields = ('machine_room_id',)
    #筛选器
    list_filter =('partner',) #过滤器
    search_fields =('name', 'address', 'img','partner','timeS','timeE','brief','tech','show','SVN','Git') #搜索字段
    date_hierarchy = 'timeS'    # 详细时间分层筛选


admin.site.register(a, ProAAdmin)

class ProBAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'img','partner','timeS','timeE','brief','tech','show','SVN','Git','imgs','file')
admin.site.register(b, ProBAdmin)

class ProCAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'img','partner','timeS','timeE','brief','tech','show','SVN','Git','imgs','file')
    search_fields = ('name', 'address')
admin.site.register(c, ProCAdmin)

class ProStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'portrait', 'QQ','blog','job','adept','other')
admin.site.register(staff, ProStaffAdmin)

class ProSoftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version', 'img','use','downFile')
admin.site.register(soft, ProSoftAdmin)
