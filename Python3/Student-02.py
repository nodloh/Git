#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

__author__='CJL'

class Student(object):
    @property
    def score(self):
        return self._score
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def resoultion(self):
        return self._width * self._height

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer')
        if value <0 or value>100:
            raise ValueError('Score must between 0-100')
        self._score=value
    
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer')
        if value <0 :
            raise ValueError('width must be >0')
        self._width=value
    
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an inteter')
        if value <0:
            raise ValueError('heigth must be >0')
        self._height=value
    

s=Student()
s.score=22
print('score=%s'  %(s.score))
s.width=11
print('width=',s.width)
s.height=11
print('heigth=',s.height)
print('resolution=',s.resoultion)
