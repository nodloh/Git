#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#利用os模块编写一个能实现dir -l输出的程序。
#实现dir -r
import time,os
def numOfFiles(path):
    num = 0
    try:
        if os.path.isdir(path):
            num = os.listdir(path).__len__()
    except BaseException as e:
            pass
    finally:
        return num

def modeToStr(mode):
    a = ['r','w','x']
    result = ""
    for i,c in enumerate(mode):
        if c == '1':
            result += a[i % 3]
        else:
            result += '-'
    return result
def listFile(path):
    print("permission\tcount\tuid\tgid\tsize\tmon\tday\tmtime\tname")
    for item in os.listdir(path):
        dir = os.path.join(path,item)
        stat = os.stat(dir)
        mtime = time.localtime(stat.st_mtime)
        param = (modeToStr(bin(stat.st_mode)[-9:]), numOfFiles(dir), stat.st_uid, stat.st_gid, stat.st_size, mtime.tm_mon, mtime.tm_mday, str(mtime.tm_hour) + ':' + str(mtime.tm_min), item)
        print('{:<9s}\t{:<5d}\t{:<2}\t{:<2}\t{:<5}\t{:<2}\t{:<2}\t{:<5s}\t{}'.format(*param))


path='/home/user/Git/Python3'
listFile(path)
