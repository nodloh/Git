#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    name1=name[0].upper()+name[1:].lower()
    return name1
#测试
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def f(x,y):
        return x*y
    return  reduce(f,L)
    
#测试
print('3*5*7*9=',prod([3,5,7,9]))
if prod([3,5,7,9])==945:
    print('测试成功')
else:
    print('测试失败！')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456 
def str2float(s):
    i=s.index('.')

    def str2int(m):
         L={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
         return L[m]
#计算前半部分
    def ff(x,y):
         return x*10+y
    s1=reduce(ff,map(str2int,s[:i]))
#计算后半部分
    def fb(x,y):
        return x*0.1+y
    s2=reduce(fb,map(str2int,s[:i:-1]))*0.1
    return s1+s2
print('str2float(\'123.456\') =', str2float('123.47'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
