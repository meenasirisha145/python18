# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:39:36 2018 by Meena Sirisha"""

import random
from random import randint
random.seed(123)
random_list = []
for i in range(1,10):
   random_list.append(randint(1,10))

random_list
range(len(random_list))
newlist=random_list[:]
newlist

num=input("enter a number:")
for i in range(len(random_list)):
    newlist[i]=random_list[i-int(num)]

print(newlist)


#%%------------------second Question-------------------%%#
l1=[]
for i in range(0,6):
    num=input("enter a number?")
    l1.append(int(num))
l2=sorted(l1)
for i in l2:
    print("*" * i)





row=input("enter a number")
i=1
j=int(row)
while i<=row:
    print((j*' '),i*'* ')
    j=j-1
    i=i+1


print((5*' ')+3*"* ")




k=int(input("Enter the number of rows"))
for i in range(0,k):
    print(' '*(k-i),'* '*(i))




num=int(input("enter length of pyramid"))
hidden_triangle = num-1
i=1
while(i<=num):
    if(hidden_triangle > 0):
        print(hidden_triangle * " ",end='')
        hidden_triangle-=1
    print(i* "* ")
    i+=1


