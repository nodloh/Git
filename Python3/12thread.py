#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start（）开始
import time,threading,multiprocessing
from multiprocessing import Pool
#新线程执行的代码
'''
def loop():
    print('@@Thread %s is running..' %threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('Thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('@@Thread %s ended' %threading.current_thread().name)

print('Thread %s is running...' %threading.current_thread().name)
t=threading.Thread(target=loop)
t.start()
t.join()
print('Thread %s is ended ' %threading.current_thread().name)

#Lock的使用
balance=0
lock=threading.Lock()

def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Balance:',balance)



#死锁(线程)
def loop():
    x=0
    while True:
        x=x^1

for i in range(multiprocessing.cpu_count()):
    t=threading.Thread(target=loop)
    t.start()

'''

#进程（process）死锁
def loop():
    x=0
    #print('Therad -', i)
    while True:
        x=x^1

#def proc(i,cpu_count):
    #print('Porcess:',i)
    #for i in range(cpu_count*2):
        #t=threading.Thread(target=loop,args=(i,))
        #t.start()


if __name__=='__main__':
    p=Pool(multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count()*2):
        p.apply_async(loop)
    p.close()
    p.join()
