#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
