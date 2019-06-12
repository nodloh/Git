#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#Get

from urllib import request

'''
with request.urlopen('https://www.douban.com') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' %(k,v))
    print('Data:',data.decode('utf-8'))

'''

def fetch_data(url):
    with request.urlopen(url) as f:
        data=f.read()
        return json.load(data.decode('utf-8'))

# 测试
URL = 'www.sohu.com'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
