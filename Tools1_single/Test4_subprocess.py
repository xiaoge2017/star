# -*- coding:utf-8 -*-
# Author:WYC
'''
读取c盘下的bat文件内容，附上sam.bat文件
@echo off
echo 显示命令行参数 %1%
set /p ver=请输入版本：
echo 输入的版本为：%ver%
'''
import subprocess

cmd = 'cmd.exe D:/star/opens.bat'
p = subprocess.Popen("cmd.exe /c" + "D:/star/opens.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

byte_data = p.stdout.read(1)

word_data = b''
while (byte_data != b''):
    word_data += byte_data
    try:
        showdata = word_data.decode('gb2312')

        print(showdata, end="", flush=True)
        word_data = b''
    except Exception as e:
        # print(e)
        a = 0
    byte_data = p.stdout.read(1)

p.wait()
print(p.returncode)