#!/usr/bin/python3
gender=input('请输入性别（M或F）:')
age=int(input('请输入年龄（1-130）:'))
if gender=='M':
    if age > 20:
        print('你已经达到法定结婚年龄了，有对象没？\n没有？抓紧啊！')
    elif age <=20:
        print('你还是个可爱的少年！！！')
else :
    if age >20:
         print('你已经达到法定结婚年龄了，有对象没？\n没有？抓紧啊！')
    elif age <=20:
        print('你还是个美丽的女孩子')

