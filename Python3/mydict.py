#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#单元测试案例
class Dict(dict):

    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" %key)

    def __setattr__(self,key,value):
        self[key]=value

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        
        if >self.score >= 80:
            return 'A'
        elif self.score >=60:
            return 'B'
        elif self.score >=0:
            return 'C'
