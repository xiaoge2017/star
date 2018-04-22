from django.contrib import admin

# Register your models here.
from imgs_db.models import Imgs,Imgs_name
class img_up(admin.ModelAdmin):
    list_display = ('id','img','single')
    # filter_horizontal = ('imgs',)
admin.site.register(Imgs, img_up)

class test_img_up(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Imgs_name, test_img_up)