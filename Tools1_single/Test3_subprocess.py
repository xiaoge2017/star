# -*- coding:utf-8 -*-
# Author:WYC
'''
读取c盘下的bat文件内容，附上sam.bat文件
echo Hello world!
echo show %1%
'''
import subprocess

cmd = 'cmd.exe c:\\sam.bat'
p = subprocess.Popen("cmd.exe /c" + "c:\\sam.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

curline = p.stdout.readline()
while (curline != b''):
    print(curline)
    curline = p.stdout.readline()

p.wait()
print(p.returncode)