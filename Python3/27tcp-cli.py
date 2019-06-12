#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#设置连接
s.connect(('127.0.0.1',9999))
#接受消息
print(s.recv(1024).decode('utf-8'))
for data in [b'cjl',b'zhangsan']:
    #发送请求
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()




