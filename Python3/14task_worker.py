#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass


#由于这个queuemanager只从网上获取queue，所以注册是只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


#连接到服务器
server_addr='127.0.0.1'
print('Connect to server %s...' % server_addr)
#端口和验证码保持和14task_master中一致
m=QueueManager(address=(server_addr,5001),authkey=b'abc')
#网络链接
m.connect()
#获取queue对象
task=m.get_task_queue()
result=m.get_result_queue()

#从task队列抓取任务数据，将结果写入到result中
for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d*%d...' %(n,n))
        r='%d*%d=%d' %(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queuee.Empty:
        print('task queue is empty.')

print('worker exit')
