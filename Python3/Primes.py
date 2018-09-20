#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#计算素数的一个方法是埃氏筛法
#定义一个序列
def odd_iter():
    n=1
    while True:
        n=n+2
        yield(n)

#定义筛选函数
def not_divisible(n):
    return lambda x:x%n>0
#定义生成器，不断返回下一个参数
def primes():
   # yield 2
    it=odd_iter()
    while True:
       n=next(it)
       yield n
       it= filter(not_divisible(n),it)

#o=odd_iter()
#for n in range(10):
#    print(next(o))

for n in primes():
    if n<=10:
        print(n)
    else:
        break
