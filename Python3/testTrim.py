#!usr/bin/env python3
#-*- coding:utf-8 -*-
def trim(s):
    if (s==''):
        raise TypeError('没有输入')
    elif (s=='    '):
        raise TypeError('空字符串')
    while(s[0]==' '):
        s=s[1:]
    while(s[-1]==' '):
        s=s[:-1]   
    return s
s=input('请输入字符串：')
print(trim(s))

