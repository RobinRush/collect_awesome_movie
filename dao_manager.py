# coding=utf-8
from pymysql import IntegrityError

from dbhelper import DBHelper


def insert_demo():
    dbhelper = DBHelper()
    dbhelper.connect()
    cur = dbhelper.get_cur()
    sql_str = """"""
    cur.execute(sql_str, None)
    cur.executemany(sql_str, [])
    dbhelper.commit()
    dbhelper.close()


def insert_dy2018(base_url, http_code):
    dbhelper = DBHelper()
    dbhelper.connect()
    cur = dbhelper.get_cur()
    sql_str = """insert into dy2018(base_url, http_code)VALUES(%s, %s)"""
    try:
        cur.execute(sql_str, (base_url, http_code))
    except IntegrityError as e:
        if e.args[0] == 1062:
            sql_str = """update dy2018 set http_code=%s where base_url=%s"""
            cur.execute(sql_str, (http_code, base_url))
            dbhelper.commit()
            dbhelper.close()
            return True
        return False
    dbhelper.commit()
    dbhelper.close()
    return True


def select_one(table):
    return select_by_cause(table, select_singe=True)


def select(table):
    return select_by_cause(table)


def select_by_cause(table, causes=None, cause_list=None, columns=None, select_singe=False):
    if columns is None:
        sql_column = '*'
    else:
        if len(columns) == 0:
            raise Exception("查询列参数为空值")
        column_list = []
        for column in columns:
            column_list.append('`%s`' % column)
        sql_column = ','.join(column_list)

    if causes is not None:
        where = '1=1 AND ( %s )' % causes
    else:
        if cause_list is not None:
            where = '1=1 AND ( %s )' % (' AND '.join(cause_list))
        else:
            where = '1=1'
    sql_str = """SELECT %s FROM %s WHERE %s""" % (sql_column, table, where)
    print(sql_str)
    dbhelper = DBHelper()
    dbhelper.connect()
    cur = dbhelper.get_cur()
    cur.execute(sql_str)
    if select_singe:
        data = cur.fetchone()
    else:
        data = cur.fetchall()
    dbhelper.close()
    return data


if __name__ == '__main__':
    data_list = select('dy2018')
    print(data_list)
    data_list = select_one('dy2018')
    print(data_list)
    data_list = select_by_cause('dy2018', cause_list=['base_url like \'%test2%\''], columns=['base_url'],
                                select_singe=True)
    print(data_list)
    pass
