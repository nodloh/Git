#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from enum import Enum,unique

@unique
class Gender(Enum):
    Male=0
    Female=1

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        #if gender==Gender.Male or gender==Gender.Female:
        #    self.gender=gender
        if isinstance(gender,Gender):
            self.gender=gender
        else:
            raise ValeError('Must be Gender vale')

#测试
bart=Student('Bart',Gender.Male)
if bart.gender==Gender.Male:
    print('测试通过')
else:
    print('测试失败')
