# -*-coding:utf-8-*-
# Author:WYC
'''
sys练习1
'''
import os,sys

def myprint(obj, end='\n'):
    sys.stdout.write(str(obj) + end)

def main():
    dir1=r'c:\temp'
    dir2=r'c:\python32'
    cmd=r'%s %s %s' % ('dir',dir1,dir2)
    os.system(cmd)

if __name__ == '__main__':
    main()
    myprint('task done')
    