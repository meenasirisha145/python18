# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:22:49 2018 by Meena Sirisha """

l=[1,2,3]
for i in range(len(l)):
    print(l[i],sep=" ",end=".")

def square(a):
    """ This will square the value """
    return(a**2)
square(3)

l.append(3)
l

%%timeit
l = []
for n in range(1000):
    l.append(n**2)

