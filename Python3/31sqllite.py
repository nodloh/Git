#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#导入sqllite驱动
import sqlite3,os
#链接到sqlite数据库test.db  如果文件不存在，会自动在当前目录创建
db_file=os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
conn=sqlite3.connect('test.db')
#创建cursor
cursor=conn.cursor()
#创建user表
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#插入一条记录
cursor.execute('insert into user (id,name) values (\'1\',\'Tom\')')
#通过rowcount获得插入的行数，即受影响的行数
cursor.rowcount
#查询记录
cursor.execute('select * from user where id=?',('1',))
#获取查询结果
values=cursor.fetchall()
print(values)
#关闭cursor
cursor.close()
#提交事物
conn.commit()
#关闭connection
conn.close()
