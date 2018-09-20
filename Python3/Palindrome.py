#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def odd_iter():
    n=0
    while True:
        n=n+1
        yield n


def circle(n):
    fronStr=str(n)
    backStr=str(n)[::-1]
    return fronStr==backStr
   # return lambda frontStr :frontStr==backStr

def is_palindrome():
    it=odd_iter()
    while True:
        #n=next(it)
        #yield n
        #it= filter(circle,it)
        return filter(circle,it)
for n in is_palindrome():
    if n <200:
        print(n)
    else:
        break
