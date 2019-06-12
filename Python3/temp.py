#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#from functools import reduce
#def su(n):
#    def g(x):
#        return x%n
#    return g
#a=su(3)
#print (a)
#print (a(9))

#print('****************')
#def sum():
#    return reduce(lambda x,y:x+y,[1,2,3,4,5])

#print(sum())

print('New Test')

class Student(object):

    def __getattr__(self,attr):
        if attr=='age':
            return lambda:22
        raise AttributeError('\'student\' object has no attribute \'%s\''%attr)
s=Student()
print(s.age())
#s.score()

print('*******************************')

class Chain(object):
    def __init__(self, path=""):
        self._path = path
    def __getattr__(self, path):
        if type(path) != str:
            raise TypeError("arg must be str")
        return Chain("%s/%s" % (self._path, path))
    __call__ = __getattr__
    def __str__(self):
        return self._path
print(Chain().status.user.timeline.list)
print(Chain().users("jack").repos)

print('%%%%%%%%%%%%%%%%%%%%%%%%%')
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'name: %s,age: %s' %(self.name,self.age)

s=Student('Tom',25)
print(s)
print('__call__函数的使用方法')
class Ainimal(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def __call__(self):
        return self._name, self._age
   # def __call__(self,value):
        #print('Name: %s,Value: %s' %(self._name,value))
a=Ainimal('Jerry',14)
print(a())
#a(2000)
print('Enumeration举例')
from enum import Enum,unique
month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','ABC'))
for name,member in month.__members__.items():
    print(name,'-->',member,',',member.value)



@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

