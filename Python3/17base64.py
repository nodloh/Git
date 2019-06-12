#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import base64
def safe_base64_decode(s):
    length=len(s)%4
    if length !=0:
        s+=b'='*(4-length)
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
