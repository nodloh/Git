#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# 指定路径下查找name文件或文件夹
import os

def find(path,name):
    try:
        for file in os.listdir(path):
            if name in file:
                print(file,'==>',os.path.join(path,file))
    except ValueError as e:
        print('No such file or directory',e)
            
            



find('/home/user/Git','13')
