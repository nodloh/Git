#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import logging,pdb
logging.basicConfig(level=logging.INFO)

#assert断言  测试
def foo(s):
    n=int(s)
    assert n != 0,'wrong'
    return 10 / n

def main():
    foo('1')

main()

#logging 测试
print('logging测试')
s='1'
n=int(s)
logging.info('n= %d' % n)
print(10 / n)

x='0'
y=int(x)
pdb.set_trace()
print(10 / n)
