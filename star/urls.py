"""star URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
# xadmin导入
import xadmin

from img_db import views as img_db
from imgs_db import views as imgs_db
from file_db import views as file_db
from files_db import views as files_db
from pro_db import views as pro_db

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^index', pro_db.index),
    url(r'^login', pro_db.login),
    # 页面
    url(r'^Get', pro_db.Get),
    url(r'^Add', pro_db.Add),
    url(r'^Del', pro_db.Del),
    url(r'^Edit', pro_db.Edit),

    # 获得
    url(r'^get_pro_a', pro_db.get_pro_content),
    url(r'^get_pro_b', pro_db.get_pro_content),
    url(r'^get_pro_c', pro_db.get_pro_content),
    url(r'^get_pro_staff', pro_db.get_pro_content),
    url(r'^get_pro_soft', pro_db.get_pro_content),
    url(r'^get_pro_info', pro_db.get_pro_content),

    # 操作
    url(r'^add_pro', pro_db.add_pro),
    url(r'^del_pro', pro_db.del_pro),
    url(r'^edit_pro', pro_db.edit_pro),

    # 打印字段名称
    url(r'^print_word', pro_db.printWord),
    # 获取当前运行函数名
    url(r'^get_current_function_name', pro_db.get_current_function_name),

    # 图片，文件上传下载
    url(r'^uploadimg', img_db.uploadImg),
    url(r'^showimg', img_db.showImg),

    url(r'^uploadfile', file_db.uploadfile),
    url(r'^showfile', file_db.showfile),

    # 多图,多文件上传
    url(r'^up_imgs', imgs_db.up_imgs),
    url(r'^upload_imgs', imgs_db.upload_imgs),

    url(r'^up_files', files_db.up_files),
    url(r'^upload_files', files_db.upload_files),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

