#!/user/bin/env python3
# _*_ coding:utf-8 _*_

#导入
from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

#创建你对象的基类
Base=declarative_base()

#定义user对象
class User(Base):
    __tablename__='user'

    #表结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    #在用户表中通过relationship（）方法来引用书表的类集合
    books=relationship('Book')

#定义Book对象
class Booos(Base):
    __tablename__='book'

    id=Column(String(20),primary_key=True)
    name=Column(String(20))

    #设置外键
    user_id=Column(String(20),ForeignKey('user.id'))

#初始化数据库链接
engine=create_engine('mysql+mysqlconnector://root:admin@localhost:3306/test')
#创建DBSession类型
DBSession=sessionmaker(bind=engine)

#添加记录
session=DBSession()
#创建新user对象
new_user=User(id='5',name='Bob')
#添加到session
session.add(new_user)
#提交
session.commit()
#查询
user=session.query(User).filter(User.id=='5').one()
#打印类型和对象的name属性
print('type:',type(user))
print('name:',user.name)

#获取用户所有的书
print(User.books)
for book in User.books:
    print('book id is:',book.id,'book name is:',book.name,'book user_id is:',book.user_id)
Book=session.query(Book).first()
pirnt(Book.user_id)
User=session.query(User).filter(User.id==Book.user_id).one()
print(User.name,User.id)
#关闭
session.close()
