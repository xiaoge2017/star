from django.db import models
from django.contrib import admin

class Imgs(models.Model):
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    img = models.ImageField(upload_to='./imgs/',verbose_name='图片地址')
    single = models.CharField(max_length=20,null=True, blank=True,verbose_name='图片名称')

    class Meta:
        verbose_name = '多图'#这里设置-在内容类型里显示
        verbose_name_plural = '图片'#这里设置-在内容类型里显示

    def __unicode__(self):  # __str__ on Python 3
        return (self.id,self.img)

    def __str__(self):
        return str(self.single)


class Imgs_name(models.Model):
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=10,verbose_name='图片库名称')
    imgs = models.ManyToManyField(Imgs, related_name='imgs',verbose_name='图片表')

    class Meta:
        verbose_name = '图片集'  # 这里设置-在内容类型里显示
        verbose_name_plural = '图片集'

    def __unicode__(self):  # __str__ on Python 3
        return (self.id,self.name,self.imgs)

    def __str__(self):
        return self.name