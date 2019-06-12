# !/usr/bin/env python3
# _*_ coding:utf-8 _*_

__author__='CJL'

class Student(object):
    count=0

    def __init__(self,name):
        self.name=name
        Student.count+=1



#测试
if Student.count !=0:
    print('测试失败！')
else:
    bart=Student('Bart')
    if Student.count !=1:
        print('False')
    else:
        lisa=Student('Lisa')
        if Student.count !=2:
            print('False again')
        else:
            print('Students:',Student.count)
            print('Success')

