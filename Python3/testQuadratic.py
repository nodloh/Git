#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
   # import math
    for i in a,b,c:
        if not isinstance(i,(int,float)):
            raise TypeError('Bad Operand Type!')
    if ( a==0 & b==0):
        raise TypeError('方程式无解')     
    elif (a==0 & b!=0) :
        print ('只有一个解：',(-c/b))
 #       raise TypeError('方程式只有一个解：') 
    else:
        p=b*b-4*a*c
        realpart=-b/(2*a)
        imagpart= math.sqrt (abs(p))/(2*a)
        if(p<0):
            print('方程有虚数解')
            print('%.3f+%.3f' % (realpart,imagpart))
        elif p>0:
            x1=realpart+imagpart
            x2=realpart-imagpart
            print('方程有实数解：')
            print('%.3f and %.3f' %(x1,x2))
        else:
            print('方程只有一个实数解：%.3f' %realpart)
