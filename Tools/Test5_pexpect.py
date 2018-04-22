# -*- coding:utf-8 -*-
# Author:WYC
'''
打开管理员cmd面板
'''
import subprocess
# 方式1：通过runas /savecred
subprocess.Popen("runas /savecred /user:Administrator cmd", shell=True)

# 方式2：通过pexpect方式
import codecs
from pexpect import popen_spawn
child=popen_spawn.PopenSpawn(r'runas /user:Administrator cmd')
# word = "输入 Administrator 的密码:".encode(encoding='UTF-8',errors='strict')
# word = word.decode(encoding='UTF-8',errors='strict')
# print (child.expect(word))
# child.send("")

'''
以管理员方式启动浏览器
'''
import os
# os.system("runas /user:Administrator \"C:\Program Files\Internet Explorer\iexplore.exe\"")