from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from imgs_db.models import Imgs_name,Imgs
import random

def up_imgs(request):
    return render(request, 'imgs_tem/up_imgs.html')

def upload_imgs(request):
    '''
        model拆分成2个表，其中一个为文件存储，一个为图集
        图集对文件存储中需要有一个字段设置为多对多的储存关系
        post后获得文件
        先对图集实例化，增加其他字段应填写的值，对这个实例存储
        再对多文件列表循环，对图片本身实例化，增加其他字段应填写的值，再对这个实例存储
        最后添加图片对应图集的关系表保存
    :param request:
    :return:
    '''
    test = Imgs_name()
    test.name = 'test' + str(random.randint(100, 900))
    test.save()
    for f in request.FILES.getlist('imgs'):
        print(f)
        empt = Imgs()
        # 增加其他字段应分别对应填写
        empt.single=f
        empt.img=f
        empt.save()
        test.imgs.add(empt)

        # File(file=f, files=test,id=1).save()
    return HttpResponse('上传成功')