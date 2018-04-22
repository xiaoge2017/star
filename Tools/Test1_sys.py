# -*- coding:utf-8 -*-
# Author:WYC
import os,sys
# 方式1：while读出来的是一起的
# try:
#     while True:
#         line = sys.stdin.readline().strip()
#         if not line:
#             break
#         print(line)
# except:
#     pass

# 方式2：读出来的一个一个的
try:
    for line in sys.stdin.readline().strip():
        if not line:
            break
        print(line)
except:
    pass