from django.contrib import admin

# Register your models here.
from files_db.models import Files,Files_name
class file_up(admin.ModelAdmin):
    list_display = ('id','file',)
admin.site.register(Files, file_up)

class test_up(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Files_name, test_up)