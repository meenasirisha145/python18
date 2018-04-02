# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:02:27 2018 by Meena Sirisha"""

import random
a=random.sample(range(1,101),100)
print(a)
print(min(a))
print(max(a))
b=sorted(a)
print(b)

def median(l):
    if len(l)%2==0:
        print(l[round(len(l)/2)])
    else:
        print((l[round((len(l)/2)-1)]+l[round(len(l)/2)])/2)


median(b)

mean=sum(b)/len(b)
mean


from random import randint

random_list = []
for i in range(1,10):
   random_list.append(randint(1,10))

# if I use sort there will be error in case of duplicates
print(sorted(random_list))
print(str(sorted(random_list)[1]) + " " + str(sorted(random_list)[-2]))

#Without sort function ??
print(random_list)
max=0
sec_max = 0
min = 99999999
sec_min = 0
for number in random_list:
   if(number>max):
        sec_max=max
        max = number
   if number > sec_max and number < max:
        sec_max = number
   if(number<min):
        sec_min=min
        min = number
   if number<sec_min and number > min:
        sec_min = number
        
        

print(str(sec_min) + " " + str(sec_max))

age=input('how old are you?')
age
















