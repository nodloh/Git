#从wsgiref模块导入
from wsgiref.simple_server import make_server
from wsgi35 import application

#创建一个服务器，地位为空，端口8000，处理函数是application
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听
httpd.serve_forever()
