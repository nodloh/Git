#!usr/bin/env python3
# _*_ coding:utf-8 _*_

from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    

    #def createWidgets(self):
    #    self.helloLabel=Label(self,text='Hello,World!')
    #    self.helloLabel.pack()
    #    self.quitButton=Button(self,text='Quit',command=self.quit)
    #    self.quitButton.pack()
'''
''' 
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.submitButton=Button(self,text='Submit',command=self.hello1)
        self.submitButton.pack()

    def hello1(self):
        name=self.nameInput.get()
        messagebox.showinfo('Meassage','Hello, %s' %name)


app=Application()
#设置窗口标题
app.master.title('Hello')
#主消息循环
app.mainloop()
