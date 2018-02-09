# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:17:59 2018 by Meena Sirisha """

import numpy as np
from numpy import *
a=np.array([[0,1,2,3],[10,11,12,13]])
a
a.shape
np.shape(a)
#%%numpy arrays

type(a)
a.size
size(a)
a.ndim
a1=array([[1,2,3],[4,5,6]],float)
a1
a1.shape
type(a1[0,0]) is type(a1[1,2])
a1.dtype
a1.dtype.type
a1.itemsize
b=a1[:,::2]
b
b[0,1]=100
b
a1
b=a1[:,::2].copy()
b[0,1]=99
b
a1
#%%fancy indexing
a=arange(0,80,10)
a
y=a[[1,2,-3]]
y
z=take(a,[1,2,-3])
z
type([a[1],a[2],a[-3]])
type(z)

ind=[1,2,-3]
x=take(a,ind)
x

#%%masking
mask=array([0,1,1,0,1,1,0,0],dtype=bool)
mask1=array([True,False,True,False,True,False,False,False],dtype=bool)
x=a[mask]
x
y=compress(mask,a)
y
z=a[mask1]
z
x=arange(0,36)
x
x=x.reshape(6,6)
x[(0,1,2,3,4),(1,2,3,4,5)]
x[3:,[0,2,5]]
x
mask=array([1,0,1,0,0,1],dtype=bool)
x[mask,2]

#%%array caluculation methods
a1
a1[0,2]=3
a1
sum(a)
%timeit sum(a1)
%timeit a1.sum()
sum(a1,axis=0)
sum(a1,axis=-1)
prod(a1,axis=0)#columnwise for axis=0
prod(a1,axis=1)#rowwise for axis=1
a1.min(axis=0)
a1.min(axis=1)
amin(a1,axis=0)
argmin(a1,axis=0)
argmin(a1,axis=1)
a1.max(axis=None)
a1.max(axis=1)
a1.argmax(axis=0)
a1.argmax(axis=1)
a1.mean(axis=0)
a1.mean(axis=1)
average(a1,axis=None)
average(a1,weights=[1,2],axis=0)
a1.std(axis=0)
a1.clip(3,5)
a1
a1.ptp(axis=0)#max-min=range
a1.ptp(axis=None)#range for entire array

#%%Comparison and Logical Operators
a=array([1,2,3,4])
b=array([4,5,6,7])
a+b
a==b
a<=b
a>=b
a!=b


a1=array([[1,2,3],[4,5,6],[7,8,9]],float)
a1
average(a1,weights=[1,2,3],axis=0)


#%%Shape Operations
a1.flatten()#converts multi-dimensional array to 1D array
a1
a1.ravel()#same as flatten but returns a view if possible
id(a1)
b=a1
id(b)
c=a1.copy()
id(c)

a1.swapaxes(0,1)#transpose
a1
a.resize(4,2)
a
np.array([1,2,3,4,5,6]).reshape(3,2)
np.array([1,2,3,4,5,6]).reshape(6,1).squeeze()
np.array([1,2,3,4,5,6]).reshape(1,6).squeeze()

a.T ##transpose
a.squeeze()#transpose
a
a.T
a[2,0]=0
a
a.nonzero()
a.cumsum(axis=None)
a1.cumprod(axis=None)
