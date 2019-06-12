#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input('From:')
password=input('Password:')
to_addr=input('To:')
smtp_server='smtp.163.com' #input('SMTP server..')

#邮件对象
msg=MIMEMultipart('alternative')
msg['From']=_format_addr('爱好者<%s>' %from_addr)
msg['To']=_format_addr('cjl <%s>' %to_addr)
msg['Subject']=Header('来自我的问候：','utf-8').encode()

#邮件正文
msg.attach(MIMEText('send with file.....','plain','utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>','html','utf-8'))

#添加附件
with open('/home/user/Git/Python3/009.png','rb') as f:
    #设置附件的MIME和文件名，类型是jpg
    mime=MIMEBase('image','png',filename='009.png')
    #必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='009.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #把附件内容读进来
    mime.set_payload(f.read())
    #用base-64编码
    encoders.encode_base64(mime)
    #添加附件
    msg.attach(mime)
try:
    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
except smtplib.SMTPException as e:
    print('邮件发送失败，case：%s' %e)
