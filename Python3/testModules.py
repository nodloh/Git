# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
'a test module'
__author__='CJL'

import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello,%s!' %args[0])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
