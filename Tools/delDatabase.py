# -*- coding:utf-8 -*-
'''
删除数据库
'''

databaseWhich='star'

def DelDatabase(databaseWhich):
    import pymysql
    pymysql.install_as_MySQLdb()
    conn = pymysql.connect(
        host='127.0.0.1',
        # port=3306,
        user='root',
        passwd='root',
        db=databaseWhich,
        charset="utf8"
    )
    cur = conn.cursor()

    Sql =str('drop database ' + databaseWhich)#  Sql = "drop database star"

    cur.execute(Sql)

DelDatabase(databaseWhich)

print ('删除完了' + databaseWhich + '数据库')