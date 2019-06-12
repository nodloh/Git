#!usr/bin/env python3
# _*_ coding:utf-8 _*_ 

#导入turtle包的所有内容
from turtle import *

#设置宽度
width(4)

#前进
forward(200)
#右转
right(90)

#颜色
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(100)
right(90)

#绘制五角星
def drawStar(x,y):
    pu()
    goto(x,y)
    pd()
    #设置其实点
    seth(90)
    for i in range(5):
        fd(40)
        rt(144)
for x in range(0,250,50):
    drawStar(x,0)


#调用done（）使得窗口等待关闭，否则将立刻关闭窗口
done()
