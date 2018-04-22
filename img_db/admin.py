from django.contrib import admin

# Register your models here.
from img_db.models import IMG
class img(admin.ModelAdmin):
    list_display = ('id','img','name')
    # filter_horizontal = ('imgs',)
admin.site.register(IMG, img)

