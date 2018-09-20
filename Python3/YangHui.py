#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def yang(max):
    L=[1]
    n=0
    while(n<max):
        yield (L)
        maxIndex=len(L)-1
        k=[L[j]+L[j+1] for j in range(maxIndex)]
        L=[1]+k+[1]
        n=n+1
    return 'None'
#for i in yang(10):
#    print(i)
g=yang(10)
while(True):
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print ('Generator return value:',e.value)
        break
