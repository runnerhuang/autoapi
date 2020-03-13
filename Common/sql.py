# -*- coding: utf-8 -*-
import pymysql
from Config.config import ReadConfig


def exec_sql(sql, db=None):
    """
    :param sql: sql language for query / update / add /delete for the test.
    :param db: database
    :return:  data for query , null for update/delete and id or other key for add.
    """
    try:
        if db:
            conn = pymysql.connect(host=ReadConfig.get_db("host"), user=ReadConfig.get_db("user"), passwd=ReadConfig
                                   .get_db("password"), port=int(ReadConfig.get_db("port")), db=db, charset='utf8')
        else:
            conn = pymysql.connect(host=ReadConfig.get_db("host"), user=ReadConfig.get_db("user"), passwd=ReadConfig
                                   .get_db("password"), port=int(ReadConfig.get_db("port")), db=ReadConfig.get_db("db_name"),
                                   charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        r = cur.fetchall()
        cur.close()
        conn.close()
        return r
    except Exception as e:
        print('Mysql Error %d: %s' % (e.args[0], e.args[1]))



