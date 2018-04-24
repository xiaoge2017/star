# _*_encoding:UTF-8_*_
'''
利用MySQLdb，创建数据库
'''

import pymysql
pymysql.install_as_MySQLdb()

def AddDatabase(db_host,db_user,db_pw,db_name):
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
