# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
from file_db.models import FILE


# Create your views here.
class FileForm(forms.Form):
    file = forms.CharField()
    name = forms.FileField()

def uploadfile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # 获取表单数据
            file = form.cleaned_data['file']
            name = form.cleaned_data['name']
            # 获取数据库数据
            user = FILE()
            user.file = file
            user.name = name
            user.save()
            return HttpResponse('file upload ok !')
    else:
        form = FileForm()
    return render_to_response('file_tem/uploadfile.html', {'form': form})

def showfile(request):
    files = FILE.objects.all()
    content = {
        'files': files,
    }
    for i in files:
        print(i.filename)

        print(i.filename.url)
    return render(request,'file_tem/showfile.html',content)
