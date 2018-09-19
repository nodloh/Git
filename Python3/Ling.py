#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def ling():
    lay=7
    for m in range((lay+1)/2):
        for b in range((lay+1)/2-m):
            print(' ',end='')
        for c in range((m*2-1)):
            print('*',end='')
        print()
    for d in range((lay+1)/2-1,0,-1):
        for b in range((lay+1)/2-d):
            print(' ',end='')
        for c in range((lay+1)/2-2+d,0,-1):
            print('*',end='')
        print()
#s=input('输入显示的层数：')
ling()
