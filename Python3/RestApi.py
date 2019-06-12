#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#动态调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    
    def __str__(self):
        return self._path

    __repr__=__str__


print(Chain().status.user.timeline.list)
