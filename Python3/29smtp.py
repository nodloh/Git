#!/usr/bin/env python3
# _*_  coding:utf-8 _*_

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#构造邮件内容
msg=MIMEText('Hello,CJL','plain','utf-8')
#输入邮箱和密码
from_addr=input('From:')
password=input('Password:')

#收件人地址
to_addr=input('To:')
#smtp服务器地址
smtp_server=input('SMTP server:')
msg['From']=_format_addr('爱好者<%s>' %from_addr)
#msg['To']=_format_addr('管理员<%s>' %to_addr)
#msg['Subject']=Header('来在smtp的问候','utf-8').encode()

#smtp默认协议端口25
server=smtplib.SMTP(smtp_server,25)
#打印出和smtp服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
