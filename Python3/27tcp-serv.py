#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket,threading,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9999))

#指定最大连接数
s.listen(5)
print('Watting for connection.....')


def tcplink(scok,addr):
    print('Accept new connection from %s:%s' %addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s' %addr)
#设定接受客户端的连接，永久性accept（）
while True:
    #接受一个连接请求
    sock,addr=s.accept()
    #创建新线程来处理TCP连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
