#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter

L=[('Bob',75),('Adam',92),('bart',66),('lisa',88)]

print(sorted(L,key=itemgetter(0)))
print(sorted(L,reverse=True,key=lambda t:t[1]))
print(sorted(L,key=itemgetter(1),reverse=True))
