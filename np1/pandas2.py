# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:40:26 2018 by Meena Sirisha """

import pandas as pd
from pandas import *
s=Series([3,7,4,4,0.3],index=['a','b','c','d','e'])
s
df=DataFrame(np.arange(9).reshape(3,3),index=['b','a','c'],columns=['Paris','Berlin','madrid'])
df
df[:2]
df[1:2]
df[:2]
df[df['Paris']>1]
df['Paris']
df.Berlin[df['Berlin']>1]=0
df
df.ix['a','Berlin']
df.ix[['b','c'],'Berlin']
df.ix['a',['Berlin','madrid']]
s.drop('d')
df.drop('Berlin',axis=1)
df.drop('c')
df
s2=Series([0,1,2],index=['a','c','f'])
s2
s+s2
s.add(s2,fill_value=0)
s.subtract(s2,fill_value=0)
s.align(s2,join='outer')
s.align(s2,join='inner')
df2=DataFrame(np.arange(12).reshape(4,3),index=['b','e','a','c'],columns=['Paris','Lisbonne','madrid'])
df2
df+df2
df.add(df2,fill_value=0)

l1=[0,1,2,3,4,5,6]
type(l1)
l2=['b','b','a','c','a','a','b']
import numpy as np
from numpy import*
d1={'data1':arange(7),'keyleft':l2}
d1

df1=DataFrame(d1,columns=['data1','keyleft'])
df1

d2={'data2':arange(4),'key':['a','b','d','a']}
df2=DataFrame(d2,columns=['data2','key'])
df2
pd.merge(df1,df2,left_on='keyleft',right_on='key',how='inner')
pd.merge(df1,df2,left_on='keyleft',right_on='key',how='outer')

merge(df1,df2)


d3={'data1':arange(6),'key':['a','b','a','a','b','c']}
d3
df3=DataFrame(d3,columns=['data1','key'])
df3
d4={'data2':arange(5),'key':['a','b','a','b','d']}
df4=DataFrame(d4,columns=['data2','key'])
df4
pd.merge(df3,df4,on='key',how='left')
pd.merge(df3,df4,on='key',how='right')


s
s.rank()
s.rank(method='first')
s.rank(method='max',ascending=False)
df
df.rank()
df.rank(axis=1)#ranking row wise
s.sort_index(ascending=False)
s.sort_index()
df.sort_index()
df.sort_index(by='Berlin')
df.sort_index(axis=1)
df.max()
df+df.max()
f=lambda x: math.sqrt(x)
df.applymap(f)
df['Berlin'].map(f)
math.factorial(5)

###Computing Descriptive Statistics####
df.describe()
df.sum()
df.sum(axis=1)
df.cov
df.corr()
df.reindex(['c','b','a','g'])
df.reindex(['c','b','a','g'],fill_value=15)
df.reindex(columns=['Varsovie','Paris','madrid'])##works with only unique index values

import os
os.getcwd()
os.chdir("F:\pywork\pyWork\pyProjects\mspython18")
data=pd.read_csv("50_Startups.csv")
data
