#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
from datetime import datetime,timedelta,timezone
'''
def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    zone=re.match(r'(\w{3})([+|-])(0[0-9]|1[0-9]|2[0-3]|[0-9]):00',tz_str)
    print(zone.groups())
    print(zone.group(0))
    print(zone.group(1))
    print(zone.group(2))
    print(zone.group(3))
    h=int(zone.group(2)+zone.group(3))
    print(h)
    zt=timezone(timedelta(hours=h))
    dt_tz=dt.replace(tzinfo=zt)
    return  dt_tz.timestamp()
'''
def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    zone=re.split(r'UTC|:',tz_str)
    #print(zone[0],zone[1],zone[2])
    h=int(zone[1])
    zt=timezone(timedelta(hours=h))
    dt_tz=dt.replace(tzinfo=zt)
    return dt_tz.timestamp()
#测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0

print('ok')
