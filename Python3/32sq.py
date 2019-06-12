#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import mysql.connector
import mysql.connector
conn=mysql.connector.connect(user='root',password='admin',database='test')
cursor=conn.cursor()

#创建表
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#插入数据
cursor.execute('insert into user (id,name) values (%s,%s)',['1','Tom'])
print(cursor.rowcount)

#cursor.close()
conn.commit()
#查询
cursor.execute('select * from user where id=%s',('1',) )
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()
