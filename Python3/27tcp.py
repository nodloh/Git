#!usr/bin/env python3
# _*_ coding:utf-8 _*_

#导入socket
import socket

#创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立链接
s.connect(('www.sina.com.cn',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close \r\n\r\n')

#接收数据
buffer=[]
while True:
    #设置一次接收的最大值
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)


#关闭链接
s.close()

header,html=data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
#把接收的数据写入文件
with open('163.html','wb') as f:
    f.write(html)
