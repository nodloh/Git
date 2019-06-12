#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import logging

#try 测试
try:
    print('try*****')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('Except:',e)
finally:
    print('Finally...')
print('End')

#调用栈 测试
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)**2

def main():
   print( bar('1'))
main()
print('End')
#记录错误 
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)**2

def main():
    try:
        print( bar(0))
    except Exception as e:
        logging.exception(e)
main()

print('END')

#抛出错误  
print('****************')
def foo(s):
    n=int(s)
    if n==0:
        raise ValueError('Invalid value: %s' %s)
    return 10/n

def bar():
    try:
        foo('10')
    except ValueError as e:
        print('Exception')
        raise

bar()

#练习  
print('练习练习练习')
from functools import reduce

def str2num(s):
    return eval(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
