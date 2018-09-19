#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-

#递归汉诺塔
def move(n,a,b,c):
    if n==1:
        print('move:',a,'---->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

#move(10,'A','B','C')
move(3,'A','B','C')
