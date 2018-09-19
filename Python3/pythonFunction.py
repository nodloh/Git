#!/usr/bin/python3
def add(a,b):
    c=a+b
    return c
print(add(3,4))

def add():
    a=1
    b=2
    print(a+b)
add()

#自定义函数
def rescursion(n):
    if n==1:
        return 1
    else:
        return 2*rescursion(n-1)
print(rescursion(10))
