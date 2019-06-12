#!/usr/bin/env python3
# _*_ coding: UTF-8 _*_
'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
'''
import re

def is_valid_email(addr):
    if re.match(r'[0-9a-zA-Z\.]+\@[a-zA-Z]{3,}\.[a-zA-Z]{3}',addr):
        return True
    else:
        return False

#测试
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr_bob@example.com')
print('ok')


#版本二可以提取出带名字的Email地址
def name_of_email(addr):
    if addr[0]=='<':
        return re.split(r'[<>]',addr)
    else:
        return re.split(r'[@]',addr)
    return None


#测试
#assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
#assert name_of_email('tom@voyager.org') == 'tom'
print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.ort'))
print('ok')
