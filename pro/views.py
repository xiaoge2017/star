# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from django.core import serializers

import os,sys,inspect
import json
import datetime,time

from pro import models
from pro.models import a as modelA
from pro.models import b as modelB
from pro.models import c as modelC
from pro.models import info as modelInfo
from pro.models import staff as modelStaff
from pro.models import soft as modelSoft

# Create your views here.
from django.db.models.sql.query import LOOKUP_SEP
from django.db.models.sql.constants import QUERY_TERMS

# 打印字段名
def printWord(request):
    import pymysql
    pymysql.install_as_MySQLdb()
    conn = pymysql.connect(
        host='127.0.0.1',
        # port=3306,
        user='root',
        passwd='910417',
        db='star',
        charset="utf8"
    )
    cur = conn.cursor()

    # 方式1
    modelWhich='pro_a'
    Sql =str('select * from '+modelWhich)
   #  Sql = "select * from pro_a"

    # 打印
    print (type(Sql))

    cur.execute(Sql)
    data_dict = []
    for field in cur.description:
        data_dict.append(field[0])
    print('打印字段名：', data_dict)
    return render(request,'print_word.html')


# 获取当前运行函数名
def get_current_function_name(request):
    print(request.path)

# ----------------------------登录----------------------------
def login(request):
    if request.method=='POST':
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('user_pwd')
        obj_name=models.info.objects.filter(name=user_name).first()
        obj_pwd=models.info.objects.filter(pwd=user_pwd).first()
        if obj_name & obj_pwd:
            print('登录成功了')
            return redirect('/get_msg/')
        else:
            return (request, 'login.html')

# -----------------------------判断表------------------------------
def isWhichTable(tableN):
    if tableN[0] == 'pro_a':
        modelN=modelA
    elif tableN[0] == 'pro_b':
        modelN=modelB
    elif tableN[0] == 'pro_c':
        modelN=modelC
    elif tableN[0] == 'pro_staff':
        modelN=modelStaff
    elif tableN[0] == 'pro_soft':
        modelN=modelSoft
    else:
        return HttpResponse('没有这个表')

    return modelN


# ------------------------获得------------------------
def get_pro_json(es,request):
    data = {}
    for e in es:

        print(request.path)
        if (str(request.path)=='/get_pro_a' or '/get_pro_b' or '/get_pro_c'):
            # 判断是否有
            if (e.imgs):
                iFimgs = e.imgs.url
            else:
                iFimgs = ''
            if (e.file):
                iFfiles = e.file.url
            else:
                iFfiles = ''
            if (e.timeS):
                iFtimeS = time.strftime("%Y-%m-%d", e.timeS.timetuple())
            else:
                iFtimeS = ''
            if (e.timeE):
                iFtimeE = time.strftime("%Y-%m-%d", e.timeE.timetuple())
            else:
                iFtimeE = ''
            data_each = {"id": e.id, "name": e.name, "address": e.address, "img": e.img.url,
                         "timeS": iFtimeS, "timeE": iFtimeE, "imgs": iFimgs, "file": iFfiles}

        elif(str(request.path)=='/get_pro_staff'):
            data_each = {"id": e.id, "name": e.name, "portrait": e.portrait.url, "QQ": e.QQ,"blog": e.blog,"job": e.job,"adept": e.adept,"other": e.other}

        elif(str(request.path)=='/get_pro_soft'):
            if (e.downFile):
                iFdownFile = e.downFile.url
            else:
                iFdownFile = ''
            data_each = {"id": e.id, "name": e.name, "version": e.version, "img": e.img.url,
                         "use": e.use, "downFile": iFdownFile}
        else:
            print('抱歉,没有这张表！')


        msgjson = {e.id: data_each}
        # print('e.file',e.file.url)
        # 字典追加
        data.update(msgjson)
    # 将python字典转换为json对象
    json_str = json.dumps(data, ensure_ascii=False)
    print(json_str)
    return json_str




def get_pro_a(request):
    # msgJson=serializers.serialize("json", models.a.objects.all(), ensure_ascii=False)
    # data1 = serializers.serialize("json", models.a.objects.filter(pk=28))
    # entry_list = list(models.a.objects.all())
    # print(entry_list[1].img.url)
    # print('entry_list', entry_list.__len__())
    es = models.a.objects.all()
    json_str = get_pro_json(es,request)
    return HttpResponse(json_str)

def get_pro_b(request):
    es = models.b.objects.all()
    json_str = get_pro_json(es,request)
    return HttpResponse(json_str)

def get_pro_c(request):
    es = models.c.objects.all()
    json_str = get_pro_json(es,request)
    return HttpResponse(json_str)

def get_pro_staff(request):
    es = models.staff.objects.all()
    json_str = get_pro_json(es,request)
    return HttpResponse(json_str)

def get_pro_soft(request):
    es = models.soft.objects.all()
    json_str = get_pro_json(es,request)
    return HttpResponse(json_str)

# ---------------增加-----------------
# 储存图片
# def handle_uploaded_file(f):
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     try:
#         path = os.path.join(BASE_DIR, 'media\\')
#         if not os.path.exists(path):
#             os.makedirs(path)
#         else:
#             file_name = str(path + f.name)
#             destination = open(file_name, 'wb+')
#             for chunk in f.chunks():
#                 destination.write(chunk)
#             destination.close()
#     except Exception (e):
#         print (e)
#     return (f.name, path)

def add_pro(request):
    if request.method == 'POST':
        # 获得数据
        tableN=request.POST.get('table_which'),
        # 判断表
        modelN=isWhichTable(tableN)
        # 对date格式的处理
        today = datetime.date.today()
        time_start = request.POST.get('timeS'),
        time_end = request.POST.get('timeE'),
        timeS = time_start[0] if time_start[0] else today
        timeE = time_end[0] if time_end[0] else today

# 多图
        img = request.FILES.get('img')
        imgs = request.FILES.getlist('imgs')
        print ('img',img)
        print ('imgs',imgs)

        print (len(imgs))
        for q in imgs:
            print (q)

        from django.views.generic.edit import FormView
        from .forms import FileFieldForm


        # for f in imgs:
        #     destination = open('media/pic_folder/' + f.name, 'wb+')
        #     for chunk in f.chunks():
        #         destination.write(chunk)
        #     destination.close()

        new_pro = modelN(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            img=request.FILES.get('img'),
            partner=request.POST.get('partner'),
            timeS=timeS,
            timeE=timeE,
            brief=request.POST.get('brief'),
            tech=request.POST.get('tech'),
            show=request.POST.get('show'),
            SVN=request.POST.get('SVN'),
            Git=request.POST.get('Git'),
            # imgs=request.FILES.getlist('imgs'),
            file=request.FILES.get('file'),
        )
        new_pro.save()
    return HttpResponse('增加完成')


# -------------------删除---------------------

def del_pro(request):
    if request.method == 'POST':
        # 获得数据
        tableN=json.loads(request.body.decode())
        tableN = (tableN['table_which'],tableN['table_which_id'])
        # 判断表
        modelN=isWhichTable(tableN)
        # 删除操作
        modelN.objects.filter(pk=tableN[1]).delete()
        return HttpResponse('删除完成')

# -------------------修改---------------------
def edit_pro(request):
    print('收到修改命令')
    if request.method == 'POST':
        # 获得数据
        tableN = (request.POST.get('table_which'),request.POST.get('table_which_id'))

        # 对date格式的处理
        today = datetime.date.today()
        time_start = request.POST.get('timeS'),
        time_end = request.POST.get('timeE'),
        timeS = time_start[0] if time_start[0] else today
        timeE = time_end[0] if time_end[0] else today

        name=request.POST.get('name'),
        address=request.POST.get('address'),
        img=request.FILES.get('img'),
        partner=request.POST.get('partner'),
        # timeS=timeS,
        # timeE=timeE,
        brief=request.POST.get('brief'),
        tech=request.POST.get('tech'),
        show=request.POST.get('show'),
        SVN=request.POST.get('SVN'),
        Git=request.POST.get('Git'),
        file=request.FILES.get('file'),

        # print(img)
        # print(file)


# 参考
#         gai=models.a.objects.get(id=5)
        # gai.name = 'Name changed again'
        # gai.save(update_fields=['name'])


        # print (img)
        # gai.img = img[0]
        # print (gai.img)
        # gai.save(update_fields=['img'])
        # print (gai)

        # 判断表
        modelN = isWhichTable(tableN)
        # 修改图片
        # gainame.name='qqqq'
        # print ('name',modelN.objects.filter(pk=tableN[1]))
        # modelN.objects.filter(pk=tableN[1])[0].save(update_fields=['name'])

        # 修改操作
        # modelN.objects.filter(pk=tableN[1]).update(name=name[0], address=address[0], partner=partner[0], timeS=timeS,
        #                                              timeE=timeE, brief=brief[0], tech=tech[0], show=show[0], SVN=SVN[0],
        #                                              Git=Git[0])
        # 表打印输出
        # v = modelN.objects.filter(pk=tableN[1])
        # for e in v:
        #     print(e.__unicode__())
        return HttpResponse('修改完成')

# ------------------------------------页面渲染-------------------------
def index(request):
    return render(request, 'index.html')

def Get_pro(request):
    return render(request, 'get_pro.html')

def Add(request):
    return render(request, 'add_pro.html')

def Del(request):
    return render(request, 'del_pro.html')

def Edit(request):
    return render(request, 'edit_pro.html')

def Search(request):
    return render(request, 'search_pro.html')

