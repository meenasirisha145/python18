# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:29:00 2018 by Meena Sirisha"""

a=list(range(1,101))
a
import random

a=random.sample(range(1,101),100)
print(a)
print(min(a))
print(max(a))
b=sorted(a)
print(b)
len(b)
b[round(len(b)/2)]
len(b)%2==0
round((len(b)/2)-1)
(b[round((len(b)/2)-1)]+b[round(len(b)/2)])/2


def median(l):
    if len(l)%2==0:
        print(l[round(len(l)/2)])
    else:
        print((l[round((len(l)/2)-1)]+l[round(len(l)/2)])/2)

median(b)

