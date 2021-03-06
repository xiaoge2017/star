from django.db import models
from django import forms
# 设置颜色的库
from django.utils.html import format_html
# Create your models here.
def createWord(models):
    GENDER_CHOICE = (
        (u'javascript', u'javascript'),
        (u'php', u'php'),
        (u'vue', u'vue'),
        (u'react', u'react'),
        (u'python', u'python'),
    )
    # gender = models.CharField(max_length=2, choices=GENDER_CHOICE)#单选
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=32, verbose_name='项目名称')
    address = models.URLField(max_length=32, verbose_name='项目地址')
    img = models.ImageField(upload_to='img', verbose_name='项目主图')
    partner = models.CharField(max_length=32, choices=GENDER_CHOICE, null=True, blank=True, verbose_name='参与者')
    timeS = models.DateField(max_length=32, null=True, blank=True, verbose_name='开始时间')
    timeE = models.DateField(max_length=32, null=True, blank=True, verbose_name='结束时间')
    brief = models.TextField(max_length=32, null=True, blank=True, verbose_name='项目简介')
    tech = models.TextField(max_length=32, null=True, blank=True, verbose_name='技术要点')
    show = models.TextField(max_length=32, null=True, blank=True, verbose_name='详细内容')
    SVN = models.URLField(null=True, blank=True, verbose_name='SVN')
    Git = models.URLField(null=True, blank=True, verbose_name='Git')
    imgs = models.ImageField(upload_to='imgs', null=True, blank=True, verbose_name='其他图')
    file = models.FileField(upload_to='./file/', null=True, blank=True, verbose_name='文件',widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.address, self.img, self.partner, self.timeS, self.timeE, self.brief, self.tech,
                self.show, self.SVN, self.Git, self.imgs, self.file)

    # 对部分字段添加颜色状态
    def colored_status(self):
        if str(self.partner) == 'wyc':
            color_code = '005296'
        else:
            color_code = '000'
            # color_code='f0f'
        return format_html(
            '<span style="color: #{};">{}</span>',
            color_code,
            self.partner,
        )

    colored_status.short_description = u'参与者'

class a(models.Model):
    GENDER_CHOICE = (
        (u'M', u'javascript'),
        (u'F', u'php'),
    )
    # gender = models.CharField(max_length=2, choices=GENDER_CHOICE)#单选
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=32, verbose_name='项目名称')
    address = models.URLField(max_length=32, verbose_name='项目地址')
    img = models.ImageField(upload_to='img', verbose_name='项目主图')
    partner = models.CharField(max_length=32, choices=GENDER_CHOICE, null=True, blank=True, verbose_name='参与者')
    timeS = models.DateField(max_length=32, null=True, blank=True, verbose_name='开始时间')
    timeE = models.DateField(max_length=32, null=True, blank=True, verbose_name='结束时间')
    brief = models.TextField(max_length=32, null=True, blank=True, verbose_name='项目简介')
    tech = models.TextField(max_length=32, null=True, blank=True, verbose_name='技术要点')
    show = models.TextField(max_length=32, null=True, blank=True, verbose_name='详细内容')
    SVN = models.URLField(null=True, blank=True, verbose_name='SVN')
    Git = models.URLField(null=True, blank=True, verbose_name='Git')
    imgs = models.ImageField(upload_to='imgs', null=True, blank=True, verbose_name='其他图')
    file = models.FileField(upload_to='./file/', null=True, blank=True, verbose_name='文件')

    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.address, self.img, self.partner, self.timeS, self.timeE, self.brief, self.tech,
                self.show, self.SVN, self.Git, self.imgs, self.file)

    # 对部分字段添加颜色状态
    def colored_status(self):
        if str(self.partner) == 'wyc':
            color_code = '005296'
        else:
            color_code = '000'
            # color_code='f0f'
        return format_html(
            '<span style="color: #{};">{}</span>',
            color_code,
            self.partner,
        )

    colored_status.short_description = u'参与者'

class b(models.Model):
    GENDER_CHOICE = (
        (u'M', u'javascript'),
        (u'F', u'php'),
    )
    # gender = models.CharField(max_length=2, choices=GENDER_CHOICE)#单选
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=32, verbose_name='项目名称')
    address = models.URLField(max_length=32, verbose_name='项目地址')
    img = models.ImageField(upload_to='img', verbose_name='项目主图')
    partner = models.CharField(max_length=32, choices=GENDER_CHOICE, null=True, blank=True, verbose_name='参与者')
    timeS = models.DateField(max_length=32, null=True, blank=True, verbose_name='开始时间')
    timeE = models.DateField(max_length=32, null=True, blank=True, verbose_name='结束时间')
    brief = models.TextField(max_length=32, null=True, blank=True, verbose_name='项目简介')
    tech = models.TextField(max_length=32, null=True, blank=True, verbose_name='技术要点')
    show = models.TextField(max_length=32, null=True, blank=True, verbose_name='详细内容')
    SVN = models.URLField(null=True, blank=True, verbose_name='SVN')
    Git = models.URLField(null=True, blank=True, verbose_name='Git')
    imgs = models.ImageField(upload_to='imgs', null=True, blank=True, verbose_name='其他图')
    file = models.FileField(upload_to='./file/', null=True, blank=True, verbose_name='文件')

    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.address, self.img, self.partner, self.timeS, self.timeE, self.brief, self.tech,
                self.show, self.SVN, self.Git, self.imgs, self.file)

    # 对部分字段添加颜色状态
    def colored_status(self):
        if str(self.partner) == 'wyc':
            color_code = '005296'
        else:
            color_code = '000'
            # color_code='f0f'
        return format_html(
            '<span style="color: #{};">{}</span>',
            color_code,
            self.partner,
        )

    colored_status.short_description = u'参与者'

class c(models.Model):
    GENDER_CHOICE = (
        (u'M', u'javascript'),
        (u'F', u'php'),
    )
    # gender = models.CharField(max_length=2, choices=GENDER_CHOICE)#单选
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=32, verbose_name='项目名称')
    address = models.URLField(max_length=32, verbose_name='项目地址')
    img = models.ImageField(upload_to='img', verbose_name='项目主图')
    partner = models.CharField(max_length=32, choices=GENDER_CHOICE, null=True, blank=True, verbose_name='参与者')
    timeS = models.DateField(max_length=32, null=True, blank=True, verbose_name='开始时间')
    timeE = models.DateField(max_length=32, null=True, blank=True, verbose_name='结束时间')
    brief = models.TextField(max_length=32, null=True, blank=True, verbose_name='项目简介')
    tech = models.TextField(max_length=32, null=True, blank=True, verbose_name='技术要点')
    show = models.TextField(max_length=32, null=True, blank=True, verbose_name='详细内容')
    SVN = models.URLField(null=True, blank=True, verbose_name='SVN')
    Git = models.URLField(null=True, blank=True, verbose_name='Git')
    imgs = models.ImageField(upload_to='imgs', null=True, blank=True, verbose_name='其他图')
    file = models.FileField(upload_to='./file/', null=True, blank=True, verbose_name='文件')

    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.address, self.img, self.partner, self.timeS, self.timeE, self.brief, self.tech,
                self.show, self.SVN, self.Git, self.imgs, self.file)

    # 对部分字段添加颜色状态
    def colored_status(self):
        if str(self.partner) == 'wyc':
            color_code = '005296'
        else:
            color_code = '000'
            # color_code='f0f'
        return format_html(
            '<span style="color: #{};">{}</span>',
            color_code,
            self.partner,
        )

    colored_status.short_description = u'参与者'

class info(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=16)
    pwd = models.CharField(max_length=16)
    save = models.CharField(max_length=16)
    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.save)

class staff(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=16)
    portrait = models.ImageField(max_length=16)
    QQ = models.CharField(max_length=16,null=True,blank=True)
    blog = models.CharField(max_length=16,null=True,blank=True)
    job = models.CharField(max_length=16,null=True,blank=True)
    adept = models.CharField(max_length=16,null=True,blank=True)
    other = models.CharField(max_length=100,null=True,blank=True)
    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.portrait, self.QQ, self.blog, self.job, self.adept, self.other)

class soft(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=16)
    version = models.CharField(max_length=16,null=True,blank=True)
    img = models.ImageField(upload_to='img')
    use = models.URLField(null=True,blank=True)
    downFile = models.FileField(upload_to = './soft/',null=True, blank=True)
    def __unicode__(self):  # __str__ on Python 3
        return (self.id, self.name, self.version, self.img, self.use, self.downFile)