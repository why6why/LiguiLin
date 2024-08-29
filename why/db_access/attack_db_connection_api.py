#!/usr/bin/env python
# -*- coding:utf-8 -*-
from db_utils import MySqLHelper
import datetime
db = MySqLHelper()

def insert_attack_log(source_ip,destination_ip,time_to_start_attack,ground_station_to_attack='',ground_station_to_be_attacked='',attack_type='tcp'):
    """
    添加攻击记录
    参数：
        source_ip：源IP
        destination_ip：目的IP
        attack_type：攻击类型
        time_to_start_attack：前端传来的攻击时间
    返回值：
        0：插入未成功
        1：插入成功
    """
    local_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql2 = 'insert into attack (source_ip,destination_ip,attack_type,time_to_start_attack,last_modified_time,create_time,delete_status,status_of_attack,ground_station_to_attack,ground_station_to_be_attacked) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    ret = db.insertone(sql2, (source_ip,destination_ip,attack_type,time_to_start_attack,local_data_time,local_data_time,'0','0',ground_station_to_attack,ground_station_to_be_attacked))
    # print(ret)
    return ret

def delete_by_id(id):
    """ 
    根据id对数据进行删除（将delete_status字段标为1）
    """
    # 如果已经被删除，则直接返回0
    if query_delete_status_by_id(id).decode() == '1':
        # print("该数据已被删除")
        return 0
    ret = update_attack_log_by_id(id=id,delete_status='1')
    return ret

def update_attack_log_by_id(id,source_ip='',destination_ip='',attack_type='',status_of_attack='',ground_station_to_attack='',ground_station_to_be_attacked='',time_to_start_attack='',time_to_end_attack='',create_time='',delete_status=''):
    """ 
    根据id进行对应的更新
    参数
        source_ip：发起攻击的源IP
        destination_ip：收到攻击的目的IP
        attack_type：攻击类型
        status_of_attack：攻击的状态，0表示正在攻击，1表示攻击结束
        ground_station_to_attack：实施攻击的地面站
        ground_station_to_be_attacked：被攻击的地面站
        time_to_start_attack：开始攻击的时间
        time_to_end_attack：结束攻击的时间
        create_time：记录创建时间
        delete_status：删除状态，0表示未删除，1表示已删除

    返回值
        0：更新未成功
        1：更新成功
    """
    # 如果已经被删除，则直接返回0
    if query_delete_status_by_id(id).decode() == '1':
        # print("该数据已被删除")
        return 0
    local_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query_sql = 'update attack set '
    if source_ip:
        query_sql += ' source_ip = \''+source_ip+'\','
    if destination_ip:
        query_sql += ' destination_ip = \''+destination_ip+'\','
    if attack_type:
        query_sql += ' attack_type = \''+attack_type+'\','
    if status_of_attack:
        query_sql += ' status_of_attack = \''+status_of_attack+'\','
    if ground_station_to_attack:
        query_sql += ' ground_station_to_attack = \''+ground_station_to_attack+'\','
    if ground_station_to_be_attacked:
        query_sql += ' ground_station_to_be_attacked = \''+ground_station_to_be_attacked+'\','
    if time_to_start_attack:
        query_sql += ' time_to_start_attack = \''+time_to_start_attack+'\','
    if time_to_end_attack:
        query_sql += ' time_to_end_attack = \''+time_to_end_attack+'\','

    query_sql += ' last_modified_time = \''+local_data_time+'\','

    if create_time:
        query_sql += ' create_time = \''+create_time+'\','
    if delete_status:
        query_sql += ' delete_status = \''+delete_status+'\','
        
    query_sql = query_sql[:-1]
    query_sql += ' where id = %s'
    print(query_sql)
    ret = db.update(query_sql,id)
    return ret

def query_delete_status_by_id(id):
    """ 
    根据id对delete_status字段进行查询
    返回值
        1为已标记删除
        0为正常数据
    """
    sql = "select delete_status from attack where id = %s"
    ret = db.selectone(sql,id)
    return ret[0]

def query_by_attack_type(attack_type='tcp'):
    """ 
    根据攻击类型查找 
    
    参数：
        attack_type: 攻击类型
    返回值：
        ret：查询的结果集
    """
    sql1 = 'select * from attack where attack_type = %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=attack_type)
    # print(ret)
    return ret

def query_by_status_of_attack(status_of_attack):
    """ 
    根据攻击状态查找
    
    参数：
        status_of_attack: 攻击状态
    返回值：
        ret：查询的结果集
    """
    sql1 = 'select * from attack where status_of_attack = %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=status_of_attack)
    # print(ret)
    return ret

def query_by_source_ip(source_ip):
    """
    根据攻击的源IP进行查找

    参数：
        source_ip: 攻击的源IP
    返回值：
        ret：查询的结果集
    """
    sql1 = 'select * from attack where source_ip = %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=source_ip)
    return ret

def query_by_destination_ip(destination_ip):
    """
    根据攻击的目的IP进行查找

    参数：
        destination_ip: 攻击的目的IP
    返回值：
        ret：查询的结果集
    """
    sql1 = 'select * from attack where destination_ip = %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=destination_ip)
    return ret

def query_by_ground_station_to_attack(ground_station_to_attack):
    """
    根据攻击的地面站进行查找

    参数：
        ground_station_to_attack: 攻击的地面站
    返回值：
        ret：查询的结果集
    """
    sql1 = 'select * from attack where ground_station_to_attack = %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=ground_station_to_attack)
    return ret

def query_by_ground_station_to_be_attacked(ground_station_to_be_attacked):
    """
    根据被攻击的地面站进行查找

    参数：
        ground_station_to_be_attacked: 被攻击的地面站
    返回值：
        ret：查询的结果集
    """
    sql1 = 'select * from attack where ground_station_to_be_attacked = %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=ground_station_to_be_attacked)
    return ret

def query_between_time_to_start_attack(begin_time,end_time):
    """ 
    通过时间区间进行查询区间内发起进攻！的数据

    参数
        begin_time：查询开始时间
        end_time：查询结束时间
    返回值
        ret：查询的结果集
    """
    sql1 = 'select * from attack where time_to_start_attack between %s and %s and delete_status = "0"'
    ret = db.selectall(sql=sql1, param=(begin_time,end_time))
    return ret

def query_recent_time_to_start_attack(time_to_start_attack='',query_size=10):
    """ 
    按攻击时间以前，倒序查询最近的记录
    
    参数
        time_to_start_attack：发起攻击时间
        query_size：所需查询数据的大小，默认为10条
    返回值
        ret：查询的结果集
    """
    sql = 'select * from attack where delete_status = "0" ' 

    if time_to_start_attack:
        sql += 'and time_to_start_attack < %s ORDER BY time_to_start_attack desc limit %s'
        return db.selectall(sql,(time_to_start_attack,query_size))
    else:
        sql += 'ORDER BY time_to_start_attack desc limit %s'
        return db.selectall(sql,query_size)

def stop_attack(id,time_to_end_attack):
    """ 
    通过id结束攻击
    参数
        time_to_end_attack：前端传来的结束攻击时间
    返回值
        0：更改失败
        1：更改成功
    """
    return update_attack_log_by_id(id,status_of_attack='1',time_to_end_attack=time_to_end_attack)

if __name__ == '__main__':
    tmp_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ret = insert_attack_log('127.0.0.1','127.0.0.1',tmp_time,'station_1','station_2','ssl')
    # ret = query_by_attack_type('ssl')
    # ret = stop_attack(17,tmp_time)
    # ret = query_by_status_of_attack('0')
    # ret = query_by_source_ip('127.0.0.1')
    # ret = query_by_destination_ip('1.2.3.4')
    # ret = query_by_ground_station_to_attack('station_1')
    # ret = query_by_ground_station_to_be_attacked('station_2')
    # ret = query_between_time_to_start_attack('2022-06-08','2022-06-26')
    # ret = update_attack_log_by_id(13,source_ip='xxxxx',destination_ip='xxxxx',attack_type='xxx',status_of_attack='xxx',ground_station_to_attack='xxxx',ground_station_to_be_attacked='xxxxxx',time_to_start_attack=tmp_time,time_to_end_attack=tmp_time,create_time=tmp_time,delete_status='1')
    # ret = delete_by_id(17)
    ret = query_recent_time_to_start_attack('2022-06-08',query_size=2)
    print(ret)
