# -*- coding:utf-8 -*-
'''
删除数据库
'''
import pymysql
pymysql.install_as_MySQLdb()

def DelDatabase(db_host,db_user,db_pw,db_name):
    conn = pymysql.connect(
        host=db_host,
        # port=3306,
        user=db_user,
        passwd=db_pw,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()

    Sql =str('drop database ' + db_name)#  Sql = "drop database star"

    cur.execute(Sql)
