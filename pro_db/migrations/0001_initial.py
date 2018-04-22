# Generated by Django 2.0.4 on 2018-04-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='a',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('address', models.URLField(max_length=32, verbose_name='项目地址')),
                ('img', models.ImageField(upload_to='img', verbose_name='项目主图')),
                ('partner', models.CharField(blank=True, max_length=32, null=True, verbose_name='参与者')),
                ('timeS', models.DateField(blank=True, max_length=32, null=True, verbose_name='开始时间')),
                ('timeE', models.DateField(blank=True, max_length=32, null=True, verbose_name='结束时间')),
                ('brief', models.TextField(blank=True, max_length=32, null=True, verbose_name='项目简介')),
                ('tech', models.TextField(blank=True, max_length=32, null=True, verbose_name='技术要点')),
                ('show', models.TextField(blank=True, max_length=32, null=True, verbose_name='详细内容')),
                ('SVN', models.URLField(blank=True, null=True, verbose_name='SVN')),
                ('Git', models.URLField(blank=True, null=True, verbose_name='Git')),
                ('imgs', models.ImageField(blank=True, null=True, upload_to='imgs', verbose_name='其他图')),
                ('file', models.FileField(blank=True, null=True, upload_to='./file/', verbose_name='文件')),
            ],
            options={
                'verbose_name_plural': '公司平台',
                'verbose_name': '公司平台',
            },
        ),
        migrations.CreateModel(
            name='b',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('address', models.URLField(max_length=32, verbose_name='项目地址')),
                ('img', models.ImageField(upload_to='img', verbose_name='项目主图')),
                ('partner', models.CharField(blank=True, max_length=32, null=True, verbose_name='参与者')),
                ('timeS', models.DateField(blank=True, max_length=32, null=True, verbose_name='开始时间')),
                ('timeE', models.DateField(blank=True, max_length=32, null=True, verbose_name='结束时间')),
                ('brief', models.TextField(blank=True, max_length=32, null=True, verbose_name='项目简介')),
                ('tech', models.TextField(blank=True, max_length=32, null=True, verbose_name='技术要点')),
                ('show', models.TextField(blank=True, max_length=32, null=True, verbose_name='详细内容')),
                ('SVN', models.URLField(blank=True, null=True, verbose_name='SVN')),
                ('Git', models.URLField(blank=True, null=True, verbose_name='Git')),
                ('imgs', models.ImageField(blank=True, null=True, upload_to='imgs', verbose_name='其他图')),
                ('file', models.FileField(blank=True, null=True, upload_to='./file/', verbose_name='文件')),
            ],
            options={
                'verbose_name_plural': '公司项目',
                'verbose_name': '公司项目',
            },
        ),
        migrations.CreateModel(
            name='c',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('address', models.URLField(max_length=32, verbose_name='项目地址')),
                ('img', models.ImageField(upload_to='img', verbose_name='项目主图')),
                ('partner', models.CharField(blank=True, max_length=32, null=True, verbose_name='参与者')),
                ('timeS', models.DateField(blank=True, max_length=32, null=True, verbose_name='开始时间')),
                ('timeE', models.DateField(blank=True, max_length=32, null=True, verbose_name='结束时间')),
                ('brief', models.TextField(blank=True, max_length=32, null=True, verbose_name='项目简介')),
                ('tech', models.TextField(blank=True, max_length=32, null=True, verbose_name='技术要点')),
                ('show', models.TextField(blank=True, max_length=32, null=True, verbose_name='详细内容')),
                ('SVN', models.URLField(blank=True, null=True, verbose_name='SVN')),
                ('Git', models.URLField(blank=True, null=True, verbose_name='Git')),
                ('imgs', models.ImageField(blank=True, null=True, upload_to='imgs', verbose_name='其他图')),
                ('file', models.FileField(blank=True, null=True, upload_to='./file/', verbose_name='文件')),
            ],
            options={
                'verbose_name_plural': '技术项目',
                'verbose_name': '技术项目',
            },
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=16, verbose_name='登录名')),
                ('pwd', models.CharField(max_length=16, verbose_name='登录密码')),
                ('save', models.CharField(max_length=16, verbose_name='保存')),
            ],
            options={
                'verbose_name_plural': '登录的用户信息',
                'verbose_name': '登录的用户信息',
            },
        ),
        migrations.CreateModel(
            name='soft',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=16, verbose_name='软件名称')),
                ('version', models.CharField(blank=True, max_length=16, null=True, verbose_name='版本号')),
                ('img', models.ImageField(upload_to='img', verbose_name='软件图')),
                ('use', models.URLField(blank=True, null=True, verbose_name='应用领域')),
                ('downFile', models.FileField(blank=True, null=True, upload_to='./soft/', verbose_name='软件')),
            ],
            options={
                'verbose_name_plural': '软件',
                'verbose_name': '软件',
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=16, verbose_name='技术人员')),
                ('portrait', models.ImageField(max_length=16, upload_to='', verbose_name='头像')),
                ('QQ', models.CharField(blank=True, max_length=16, null=True, verbose_name='QQ')),
                ('blog', models.CharField(blank=True, max_length=16, null=True, verbose_name='博客')),
                ('job', models.CharField(blank=True, max_length=16, null=True, verbose_name='工作职位')),
                ('adept', models.CharField(blank=True, max_length=16, null=True, verbose_name='擅长领域')),
                ('other', models.CharField(blank=True, max_length=100, null=True, verbose_name='其他')),
            ],
            options={
                'verbose_name_plural': '技术人员',
                'verbose_name': '技术人员',
            },
        ),
    ]
