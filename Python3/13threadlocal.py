#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#threadlocal使用
import threading

#创造全局变量  Threadlocal对象

'''
local_school=threading.local()


def process_student():
    std=local_school.student
    print('hello %s in %s'  %(std,threading.current_thread().name))

def process_thread(name):
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('Tom',),name='Thread-1')
t2=threading.Thread(target=process_thread,args=('Jerry',),name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()

'''

local = threading.local()
class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def getInfo():
    stu = local.student
    print('this is %s, %d, %d in %s' %(stu.name, stu.age, stu.score, threading.current_thread().name))

def setInfo(name, age, score):
    local.student = Student(name, age, score)
    getInfo()

t1 = threading.Thread(target=setInfo, args=('Alice', 25, 88), name='Thread_1')
t2 = threading.Thread(target=setInfo, args=('Bob', 27, 90), name='Thread_2')
t1.start()

t2.start()
t1.join()
t2.join()
print('print complete...')

#print(threading.current_thread())
#print(threading.current_thread().getName())
#print(threading.current_thread().name)


global_data=threading.local()

def show():
    print(threading.current_thread().getName(),global_data.num)

def thread_cal():
    global_data.num=0
    for _ in xrange(1000):
        global_data.num +=1
    show()

threads=[]
for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()

#print('Main thread:',global_data.__dict__)

