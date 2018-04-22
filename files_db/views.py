from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from files_db.models import Files_name,Files
import random

def up_files(request):
    return render(request, 'files_tem/up_files.html')

def upload_files(request):
    test = Files_name()
    test.name = 'test' + str(random.randint(100, 900))
    test.save()
    for f in request.FILES.getlist('files'):
        empt = Files()
        empt.file = f
        empt.save()
        test.files.add(empt)
        # File(file=f, files=test,id=1).save()
    return HttpResponse('上传成功')