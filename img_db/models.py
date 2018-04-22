from django.db import models

# Create your models here.
class IMG(models.Model):
    img = models.ImageField(upload_to='img',verbose_name='id')
    name = models.CharField(max_length=100,verbose_name='图片名称')
    class Meta:
        verbose_name = '单图'  # 这里设置-在内容类型里显示
        verbose_name_plural = '单图'