from django.contrib import admin

# Register your models here.
from file_db.models import FILE
class file(admin.ModelAdmin):
    list_display = ('id','file','name')
admin.site.register(FILE, file)

