# # coding:utf-8
# from django.db import models
# from django_thumbs.db.models import ImageWithThumbsField
# import os, datetime, uuid
#
#
# def generate_filename(instance, filename):
#     """
#     安全考虑，生成随机文件名
#     """
#     directory_name = datetime.datetime.now().strftime('photos/%Y/%m/%d')
#     filename = uuid.uuid4().hex + os.path.splitext(filename)[-1]
#     return os.path.join(directory_name, filename)
#
#
# class Photo(models.Model):
#     name = models.CharField('名称', max_length=10)
#     photo = ImageWithThumbsField('照片', upload_to=generate_filename, sizes=((150, 150),))
#
#     def __unicode__(self):
#         return self.photo.url_150x150
#
#     class Meta:
#         verbose_name_plural = verbose_name = '照片'