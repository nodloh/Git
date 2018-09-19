#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#默认参数
def enroll(name,gender,age=6,city='ZheJiang'):
    print('name',name)
    print('gender',gender)
    print('age',age)
    print('city',city)
#******    
def add_end(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L

#可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#关键字参数
def person(name,age,*,city,job):
   # if 'city' in other:
    #    pass
    #if 'job' in  other:
     #   pass
    print('name',name,'age',age,'city',city,'job',job)

