#!/usr/bin/env python3
# -*- conding: utf-8 -*-
def findMinAndMax(L):
    if (len(L)==0):
   #     print('None,None')
        return(None,None)
   # elif (len(L)==1):
    #    return(L[0],L[0])
    else:
        min=L[0]
        max=L[0]
        for i in L:
            if i<min:
                min=i
            if i>max:
                max=i
        return(min,max)
#l=input('请输入比较列表：')
#print(findMinAndMax(l))

