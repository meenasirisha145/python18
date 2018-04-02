# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:14:31 2018 by Meena Sirisha"""

#%%Group by
import numpy as np
import pandas as pd

#Marks
rng=np.random.RandomState(42)
marks=pd.Series(rng.randint(50,100,11))
marks
marks.sum()
marks.std()


#Dictionary
dict(x=1,y=4)


#Groupwise
df=pd.DataFrame({'A':rng.randint(1,10,6),'B':rng.randint(1,10,6)})
df
df.sum(axis=0)
df.sum(axis=1)
df.mean()
df.mean(axis=0)
df.mean(axis='columns')
df.mean(axis='rows')
df.describe()

#GroupBy
# Split -Apply -Combine
#Repeat
['A','B','C']*2
np.repeat(['A','B','C'],2)
np.repeat(['A','B','C'],[1,2,3])

df1=pd.DataFrame({'key':['A','B','C']*2,'data1':range(6),'data2':rng.randint(0,10,6)},columns=['key','data1','data2'])
df1
df1.groupby('key').sum()
grouped=df1.groupby('key')
grouped.sum()

df1.groupby('key').aggregate(['min','max','median'])
df1.groupby('key').aggregate([np.median,'median'])#error they are repeating
df1.groupby('key').aggregate({'data1':'min','data2':'max'})
df1.groupby('key').aggregate([np.median])
df1.groupby('key').aggregate({'data1':['min','mean'],'data2':['min','max']})

#Filter :Select Column

df1.filter(items=['data1','key'])
df1.filter(like='0',axis=0)#row by position
df1.filter(like='2')
df1.filter(like='e',axis=1)
df1.filter(like='d',axis=1)#col by position
df1.groupby('key').std()


#Lambda
df1['data2'].mean()
df1['data1'].mean()
df1
grouped.filter(lambda x : x['data2'].mean()>4)#list the elements of group whose mean is >4
grouped.filter(lambda x : x['data2'].std()>4)
grouped.transform(lambda x : x-x.mean())


#Apply Method
grouped.apply(lambda x : x['data2']*2)


#Provide Group Keys
df1.groupby('key').sum()
df1.groupby(df1['key']).sum()


df2=df1.set_index('key')
df2

newmap={'A':'Post Graduate','B': 'MSc','C': 'BSc'}
df2.groupby(newmap).sum()
df2.groupby(str.lower).mean()
df2.groupby([str,str.lower,newmap]).mean()#str =index


#Stack

df2.groupby('key').sum().unstack()
