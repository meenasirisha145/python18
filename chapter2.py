# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:52:04 2018 by Meena Sirisha"""

name="meena sirisha"
name.title()
name.lower()
name.upper()
f_name="meena"
l_name="sirisha"
full_name=f_name+" "+l_name
full_name
print("Hello"+" "+full_name.title()+".")
print("Languages:\nPython\nC\nJavaScript")
print("Skills:\nC\tC++\tJava")
lan=" Machine Learning using Python "
lan
lan.rstrip()
lan
lan.lstrip()
lan.strip()
lan
lan=lan.strip()
lan
message = 'One of Python\'s strengths is its diverse community.'
print(message)

a="Machine Learning"
b=1
print(a+" "+str(b)+"st class")
import this

#%%---------------CHAPTER-3----------------------%%#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[2].title())
bicycles[0]="hero"
print(bicycles)
bicycles.append("ladybird")
print(bicycles)
bicycles.pop()
bicycles
bicycles.sort()
bicycles
bicycles.insert(2,"ladybird")
bicycles
del(bicycles[1])
bicycles
bicycles.pop(1)
bicycles
bicycles.remove("redline")
bicycles

#%%%------------------Practise Exercise----------------------%%%#

guests=["apoorva","shruti","soumya","aadhya"]
for guest in guests:
    print(guest.title() + ","+" " "I kindly invite you to the dinner at my home")

print("Task Completed : Inviting People")
print("oh Shruti is unable to attend the dinner")
#Replacing Shruti with Priya

guests[1]="Priya"
guests
for guest in guests:
    print(guest.title() + ","+" "+ "I kindly invite you to the dinner at my home")
 
for guest in guests:
    print(guest.title() + ","+" " +"I found a bigger dining table")
    
guests.insert(0,"Pragati")
guests.insert(2,"ramya")
guests.append("ujala")
guests
for guest in guests:
    print(guest.title() + ","+" "+ "I kindly invite you to the dinner at my home")
    
print("I can invite only two people for the dinner")
for guest in guests[2:]:
    print(guest.title()+","+" "+"I can't invite you to the dinner")
    guests.pop()
guests
for guest in guests:
    print(guest.title() + ","+" "+ "you are still invited to the dinner at my home")


del(guests)


places=["US","UK","Canada","Finland","Singapore"]
places
sorted(places)
