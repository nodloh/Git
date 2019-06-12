#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import os
def modeToStr(mode):
    a=['r','w','x']
    result=''
    for i,c in enumerate(mode):
        if c=='1':
            result +=a[i%3]
        else:
            result +='_'
    return result

stat=os.stat('/home/user/Git/Python3/09-chmod.py')
mode=bin(stat.st_mode)[-9:]
print(mode)
print(modeToStr(mode))
