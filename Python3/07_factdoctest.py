#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#class DocTest():

def fact(n):
    '''
    Calculate 1*2*3...*n
    >>> fact(1)
    1
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError

    '''
    if n<1:
        raise ValueError()
    if n==1:
        return 1
    return n * fact(n-1)


if __name__=='__main__':
    import doctest
    doctest.testmod()
