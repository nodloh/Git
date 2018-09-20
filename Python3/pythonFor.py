#!/usr/bin/python3
for i in 'PYTHON':
    print(i)
#  range()
for i in range(1,10,3):
 
    print (i)
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        sum =i*j
        print('%d *%d =%d    ' %(j,i,sum),end='')
    print('\n')

