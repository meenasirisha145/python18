# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:52:24 2018 by Meena Sirisha """



##lists
x=[1,2,3]
x
print(x)

x=[1,8,5,6,8,4,5,6,4]
x[0]
len(x)
sum(x)
max(x)
min(x)
for i in range(len(x)):
    print(x[i],end=',')
    
if 3 in x:
    print("yes")
else:
    print("no")

x.append(3)
x
sorted(x)
x.index(5)

