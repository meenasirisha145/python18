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

#lists are mutable
l=[1,2,"a"]
l
type(l)
l[1]=3
l

#tuples are immutable list but faster and consumes less memory
t=(1,2,"a")
type(t)
t[2]=3##does not support item assignment


#Dictonaries

d={"a":1,"b":2,3:"d"}
d
type(d)
d["b"]=6
d


##sets
s1={1,2,3}#unordered so slicing cannot be done

#frozen set
f=frozenset({3,8,4,6})
type(f)#immutable



###practise for lists
b="nice"
a="ls"
my_list=['my','list',a,b]
my_list
my_list2=[[4,5,6,7],[3,4,5,6]]
my_list2
my_list[1]
my_list[-3]
my_list[1:3]
len(my_list)
my_list[-len(my_list)]
my_list[1:]
my_list[:3]
my_list2[1][0]
my_list2[0][2]
my_list2[0][:3]
my_list+my_list
my_list+my_list2
my_list*2
my_list2[1][1]>4
my_list.index(a)
my_list.count(a)
my_list.append("!")
my_list
my_list.extend("!")
my_list
my_list.count("!")
my_list.sort()
my_list
my_list.remove("!")
my_list
my_list.pop()
my_list


x=[i for i in range(10)]
print(x)


squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)

l3=[1,2,"a",True]
sum(l3[0:2])
l1=[1,2,3,4,5]
l2=[1,2,3,"a",True]
l3=[i for i in range(5)]
l3
type(l1)
type(l2)
type(l3)
type(l3[4])
for i in range(len(l2)):
    print(type(l2[i]))

for i in range(len(l2)):
    print(type(l2[i]),end=' ')


l=l1+l2
l
sum(l)
sum(l[1:4])
l[len(l)-2].upper()
len(l)

#list inside a list
l4=[1,2,[l2]]
l4
print(l4)
l4[1]
l4[2]
l4[2][0]
l4[2][0][0]

l4=[1,2,l2]
l4[2][0]

#dictionaries
d1={1:'appu',2:'meenu',3:'hitesh',4:'lalit',5:'achal','dean':'dhiraj sir','l':[1,2,3]}
d1
d1.keys()
d1.values()
d1.items()
d1[1]
d1['dean']
d1['l']
d1['f']=d1.pop(4)
d1
d1['f']='lalit sahni'
d1
d1['l'][1]='z'
d1
for key in d1:
    print(key,end=' ')
    print(d1[key],end=' ')

#list to a set
l1=[1,2,3,4,5,5]
s1=set(l1)
type(s1)
s1
a=set([1,2,3,4,5,6])
a
b=set([1,2,"a",True,l4])
b
s2=set()
s2.add(4)
s2.add(5)
s2
a|b#union
a&b#intersection
a<b#subset
a.issubset(b)
a-b#difference
b-a
a.issuperset(b)
a^b
len(a)

c=set([4,5,3,2,1,6])
sorted(c)
s3=set([1,2,4,'apple','Tom',3])
s4=set([1,None,3])
s4
all(s4)
all(s3)
s3.remove(1)
s3
s3.remove(1)
s3.discard(1)
s3.pop()
s3
s5=s3|s4
s5
s3.update(s4)
s3
s3.isdisjoint(s4)
