# -*-coding:utf-8-*-
# Author:WYC
'''
python调用Shell脚本，有两种方法：os.system(cmd)或os.popen(cmd),前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容。
'''
import os,sys,subprocess
# os.system('date')#设置为GBK即可解决乱码问题

def INITAPP(my_file_ROOT,operate0,operate1,operate2):
    print(os.getcwd())
    os.chdir(my_file_ROOT)#切换工作目录
    # os.chdir('C:/Users/wyc/Desktop/star')#切换管理员工作目录
    print('切换工作路径',os.getcwd())
    os.system(operate0)
    os.system(operate1)
    os.system(operate2)

# os.system('cmd')
# os.system(operate4)



# import subprocess
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'python manage.py createsuperuser')
# print(output)
# print('Exit code:', p.returncode)


# import subprocess,codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# sys.stdout.write(operate4)


