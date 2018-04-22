from django.db import models
from django.contrib import admin

class Files(models.Model):
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    file = models.FileField(upload_to='./files/',verbose_name='文件名称')
    class Meta:
        verbose_name = '文件'  # 这里设置-在内容类型里显示
        verbose_name_plural = '文件'
    def __unicode__(self):  # __str__ on Python 3
        return (self.id,self.file)

class Files_name(models.Model):
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=10,verbose_name='文件集名称')
    files = models.ManyToManyField(Files, related_name='files',verbose_name='文件')
    class Meta:
        verbose_name = '文件集'  # 这里设置-在内容类型里显示
        verbose_name_plural = '文件集'
    def __unicode__(self):  # __str__ on Python 3
        return (self.id,self.name,self.files)