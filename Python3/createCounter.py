#!/usr/bin/env python3
# _*_ coding:utf-8 *-*
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    L=[0]
    def counter():
        #for n in range(1,10):
        L[0]+=1
        return L[0]
    return counter
#方法二
def createCounter2():
    def iter():
        n=1
        while True:
            yield n
            n=n+1
    it=iter()
    def counter():
        return next(it)
    return counter
#方法三
def createCounter3():
    n=1
    def counter():
        nonlocal n
        n+=1
        return n
    return counter


counterA=createCounter()
counterB=createCounter2()
counterC=createCounter3()
print(counterA(),counterA())
print(counterB(),counterB(),counterB())
print(counterC(),counterC(),counterC())
