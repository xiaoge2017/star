# Generated by Django 2.0.4 on 2018-04-23 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('file', models.FileField(upload_to='./files/', verbose_name='文件名称')),
            ],
            options={
                'verbose_name_plural': '文件',
                'verbose_name': '文件',
            },
        ),
        migrations.CreateModel(
            name='Files_name',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=10, verbose_name='文件集名称')),
                ('files', models.ManyToManyField(related_name='files', to='files_db.Files', verbose_name='文件')),
            ],
            options={
                'verbose_name_plural': '文件集',
                'verbose_name': '文件集',
            },
        ),
    ]
