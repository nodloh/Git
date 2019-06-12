#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from multiprocessing import Process,Pool,Queue
import os,time,random,subprocess
"""
print('Process (%s) start....'%os.getpid() )

pid=os.fork()
if pid==0:
    print('I am child process (%s) and my parent is (%s)' %(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s)' %(os.getpid(),pid))


#multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束
#待执行的子进程

def run_proc(name):
    print('Run child process %s (%s)..' %(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s' %os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

#如果要启动大量的子进程，可以用进程池(pool)的方式批量创建子进程

def long_time_task(name):
    print('Run task %s (%s)...' %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds' %(name,(end-start)))


if __name__=='__main__':
    print('Parent process %s' %os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')

#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
print('$nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

#如果子进程需要输入，可以通过communicate（）方法实现
print('*************************8')
print('nslookup www.python.org')

p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)
"""
#Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#写数据进程执行的代码
def write(q):
    print('Process to write: %s' %os.getpid())
    for value in ['a','b','c']:
        print('Put %s to queue' %value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print('Process to read: %s' %os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue' %value)


if __name__=='__main__':
    #父进程创建Queue，并传递给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

