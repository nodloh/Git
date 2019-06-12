# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
import functools,time
def log(func):
    @functools.wraps(func)
    def wrapper(*arg,**kw):
        print('Call %s()' %func.__name__)
        return func(*arg,**kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg,**kw):
            print('%s %s()' %(text,func.__name__))
            return func(*arg,**kw)
        return wrapper
    return decorator
@log
def now():
    print('This is decorator!!')
print(now.__name__)
f=now()
print(f)

print('课后练习:设计一个decorator, 它可作用于任何函数上，并打印该函数的执行时间')

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*arg,**kw):
        start=time.time()
        fn(*arg,**kw)
        end=time.time()
        print('%s execute in %s ms' %(fn.__name__,end-start))
        return fn(*arg,**kw)
    return wrapper
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y
f=fast(11,22)
print(f)


print('函数调用前后打印begin call 和 end call,且通杀log和log(execute)')
def log3(args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg,**kw):
            if not hasattr(args,'__call__'):
                print(args)
            print('Begin call %s' %func.__name__)
            #print(args)
            func(*arg,**kw)
            print('End call %s' %func.__name__)
            #return func(*arg,**kw)
        return wrapper
    if hasattr(args,'__call__'):
    #if args=='':
        return decorator(args)
    else:
        return decorator
@log3
def now():
    print('no args')

now()

@log3('Execute')
def now2():
    print('one args')

now2()
