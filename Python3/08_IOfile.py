#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#请将本地一个文本文件读为一个str并打印出来
fpath=r'/home/user/Git/Python3/temp.py'

with open(fpath,'r',encoding='utf-8',errors='ignore') as f:
    print(f.read())
