# coding=utf-8

import pymysql
from mysql_cfg import *


class DBHelper:
    def __init__(self):
        self._conn = None

    def connect(self):
        self._conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbname,
                                     charset=dbcharset)

    def get_cur(self):
        return self._conn.cursor()

    def commit(self):
        self._conn.commit()

    def close(self):
        self._conn.close()

    def rollback(self):
        self._conn.rollback()
