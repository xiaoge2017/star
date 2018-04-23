# _*_encoding:UTF-8_*_
'''
利用MySQLdb，创建数据库
'''

import pymysql
pymysql.install_as_MySQLdb()
db_host = '127.0.0.1'
db_user = 'root1234'
db_pw = 'root1234'
db_name = 'star5678'

def addDatabase(db_host,db_user,db_pw,db_name):
    try:
        print('try')
        # 数据库连接
        conn = pymysql.connect(db_host,db_user,db_pw, charset='utf8')
        # 创建游标，通过连接与数据通信
        cur = conn.cursor()
        # 执行sql语句
        cur.execute('show databases')
        rows = cur.fetchall()
        for row in rows:
            tmp = "%2s" % row
        # 判断数据库是否存在
        if db_name == tmp:
            cur.execute('drop database if exists ' + db_name)
        cur.execute('create database if not exists ' + db_name)
        # 提交到数据库执行
        conn.commit()
    except pymysql.Error:
        print ("Mysql Error %d: %s" % (pymysql.Error.args[0], pymysql.Error.args[1]))
    finally:
    # 关闭数据库连接
        conn.close()
addDatabase(db_host, db_user, db_pw,db_name)
print ('创建完了' + db_name + '数据库')