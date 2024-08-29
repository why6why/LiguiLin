#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .db_utils import MySqLHelper

db = MySqLHelper()


def query_all():
    sql = 'select * from flows'
    ret = db.selectall(sql)
    return ret


def insert_one(src_ip, dest_ip, label, index, attack_frequency):
    sql = 'insert into flows (src_ip,dest_ip,label,type_index,attack_frequency) VALUES (%s,%s,%s,%s,%s)'
    ret = db.insertone(sql, (src_ip, dest_ip, label, index, attack_frequency))

    return ret


def insert_many(li):
    # 增加多条
    sql1 = 'insert into flows (src_ip,dest_ip,label,type_index,attack_frequency) VALUES (%s,%s,%s,%s,%s)'
    ret = db.insertmany(sql1, li)
    return ret


def truncate_table_flows():
    sql = 'truncate table flows'
    ret = db.execute(sql)


if __name__ == '__main__':
    # ret = insert_one('127','128','t',3,3.4)
    # ret = query_all()
    # ret = truncate_table_flows()
    li = ((b'test_2', b'test_2', b'test_2', 2, 2), (b'test_1', b'test_1', b'test_1', 1, 1))
    # new_li = []
    # print(type(new_li))
    # for l in li:
    #     # new_li.append(str(list(l[0],l[1],l[2],l[3],l[4],l[5])))
    #     # print(l[1].decode(),l[2].decode(),l[3].decode(),l[4],l[5])
    #     tmp_li = []
    #     tmp_li.append(l[0].decode())
    #     tmp_li.append(l[1].decode())
    #     tmp_li.append(l[2].decode())
    #     tmp_li.append(l[3])
    #     tmp_li.append(l[4])
    #     new_li.append(tmp_li)
    # print(new_li)
    # ret = insert_many(new_li)
    ret = insert_many(li)
    print(ret)
