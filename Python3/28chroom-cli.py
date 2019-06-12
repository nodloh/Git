#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/12/6 14:10
# @Author : Mr.Zuo
# @File : chatrmser.py
# @desc : 简易聊天室
import socket
import threading
import logging

# 客户端 数据分隔符
CLIENT_SPLIT = ']]][[['
# 消息编码
MESSAGE_ENCODING = 'utf-8'
# TCP最大等待连接数
TCP_MAX_WAITING = 10
# 一次读取字节数
BUFFER_SIZE = 1024
# 默认主机名和端口
DEFAULT_ADDRESS = ('127.0.0.1', 8080)
logging.basicConfig(level=logging.INFO)

# 聊天室客户端
class Client(socket.socket):

    def __init__(self, name, address=DEFAULT_ADDRESS):
        super(Client, self).__init__(type=socket.SOCK_DGRAM)
        # 服务器地址
        self.__address = address
        # 聊天室昵称
        self.__name = name

    # 启动客户端
    def start(self):
        logging.info('【客户端已启动】')
        # 启动后向服务器发送昵称和客户端地址
        self.sendto(self.__name.encode(MESSAGE_ENCODING), self.__address)
        # 启动子线程接收服务器消息
        t = threading.Thread(target=self.recv_handler)
        t.start()
        while True:
            msg = input()
            self.send_msg(msg)

    # 发送消息
    def send_msg(self, msg):
        # 将用户昵称加入消息
        data = (self.__name+CLIENT_SPLIT+msg).encode(MESSAGE_ENCODING)
        # 发送消息至服务器
        self.sendto(data, self.__address)
        self.show_msg(data)

    # 打印消息
    def show_msg(self, data):
        name, msg = data.decode(MESSAGE_ENCODING).split(CLIENT_SPLIT)
        if name == 'sys':
            print('----------%s----------' % msg)
        elif name == self.__name:
            print('%s：%s' % (name, msg))
        else:
            print('\t\t\t\t\t\t%s：%s' % (msg, name))

    # 接收服务器发送的数据
    def recv_handler(self):
        while True:
            data = self.recv(BUFFER_SIZE)
            self.show_msg(data)


c = Client('Alex1', address=('127.0.0.1', 8080))

c.start()
