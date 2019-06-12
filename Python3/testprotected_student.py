#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

__author__='cjl'

class Student(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender
        
    def set_name(self,name):
        self.__name=name
        
    def set_gender(self,gender):
        if gender=='Male':
            self.__gender=gender
        elif gender=='Female':
            self.__gender=gender
        else :
            raise ValueError('Bad Value!')
        
bart=Student('Tom','Male')
print('bart.get_name()', bart.get_name())
bart.set_gender('Female')
print('bart.get_gender',bart.get_gender())

print('DO NOT USER bart._Student__name', bart._Student__name)
