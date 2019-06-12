#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from html.parser import HTMLParser
from urllib import request
import urllib,ssl,re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__flag='' #设置标志位
    def handle_starttag(self,tag,attrs):
        #attr里面有一个是dict组成的list，筛选找到和是的标签位置，然后把标志位设为相应的
        if tag=='h3' and ('class','event-title') in attrs:
            self.__flag='title'
        if tag=='time':
            self.__flag='time'
        if tag=='span' and ('calss','sya-no-more') in attrs:
            self.__flag='year'
        if tag=='span' and ('class','event-location') in attrs:
            self.__flag='location'

    def handle_endtag(self,tag):
        #html一般是<>??</>这样格式，在</>处将标志位清空
        self.__flag=''

    def handle_data(self,data):
        if self.__flag=='title':
            print(data)
        if self.__flag=='time':
            print(data)
        if self.__flag=='year':
            #还有2个符合tag=='span' and ('class','say-no-mor')筛选条件的，但并不是我们需要的year，所以需要用正则过滤掉
            if re.match(r'\s\d{4}',data):
                print(data)
        if self.__flag=='location':
            print(data)
            print('-------------------')

context=ssl._create_unverified_context() #ssl验证问题
parser=MyHTMLParser()
url='https://www.python.org/events/python-events/'
with urllib.request.urlopen(url,context=context) as f:
    data=f.read()
    parser.feed(data.decode('utf-8'))

