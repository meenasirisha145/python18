# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:19:48 2018 by Meena Sirisha """


import numpy as np
np.__version__
np.abs
np.array([1,4,2,5,3])
l=[i for i in range(5)]
l
l
np.full((3,5),3.14)
x=np.arange(0,20,2)
len(x)

np.linspace(0,1,5)
np.random.random((3,3))
np.random.normal(0,1,(3,3))
np.random.randint(0,10,(3,3))
np.eye(3)
np.empty(3)
np.zeros(10)
np.random.seed(0)
x1=np.random.randint(10,size=6)
x2=np.random.randint(10,size=(3,4))
x3=np.random.randint(10,size=(3,4,5))
x1
x2
x3
x1,x2,x3
x3.ndim
x3.shape
x3.size
x3.itemsize
x3.nbytes
x2[0][2]
x3[2][1][0]
x=np.arange(10)
x
x[:5]
x[5:]
x[4:7]
x[::2]
x[1::2]
x[0::2]
x[1::3]
x[::3]
x[::-1]
x[::-3]
x2
x2[:2,:3]#two rows and three columns
x2[:3,::2]
x2[:3,::3]
x2[::-1,::-1]
x2[:,0]
x2[0,:]
y=x2[:2,:2]
y[0][0]=25
y
x2
z=x2[:2,:2].copy()
z
z[0][0]=52
z
x2
