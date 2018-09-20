#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterator,Iterable

def g():
    yield 1
    yield 2
    yield 3

print('Iterable?[1,2,3]',isinstance([1,2,3],Iterable))
print('Iterable?g()',isinstance(g(),Iterable))
print('Iterator? iter([1,2,3])',isinstance(iter([1,2,3]),Iterator))
print('Iterator?g()',isinstance(g(),Iterator))


#iter list
for x in [1,2,3,4,5]:
    print(x)


for x in iter([1,2,3,4,5]):
    print(x)

print('next():')
it=iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

    
