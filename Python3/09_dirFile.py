#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os
def search(a,b):
    for file in os.listdir(a):
        if os.path.isfile(os.path.join(a,file)):
            if b in file:
                print(file,'=>',os.path.join(a,file))
        else:
            search(os.path.join(a,file),b)
 
#if __name__ == "__main__":
search('.','.py')
