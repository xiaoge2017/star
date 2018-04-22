# from __future__ import unicode_literals
from django.db import models

# Create your models here.
class FILE(models.Model):
    file = models.CharField(max_length = 30)
    name = models.FileField(upload_to = './file/')

    class Meta:
        verbose_name = '单文件'  # 这里设置-在内容类型里显示
        verbose_name_plural = '单文件'

    def __unicode__(self):
        return (self.file,self.name)
