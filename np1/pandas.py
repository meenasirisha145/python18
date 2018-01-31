# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:09:02 2018 by Meena Sirisha """


#####-----PANDAS-----########
import pandas as pd
pd.__version__
import tensorflow as tf
tf.__version__
data=pd.Series([0.25,0.5,0.75,1.0])
data
data.values
data[1]
data=pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
data[0]
data['a']
data
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=[2, 5, 3, 7])
data
data[5]
population_dict = {'California': 38332521,'Texas': 26448193,'New York': 19651127,
                   'Florida': 19552860,'Illinois': 12882135}
population = pd.Series(population_dict)
population


pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
#Notice that in this case, the Series is populated only with the explicitly identified keys

#data can be a dictionary, in which index defaults to the sorted dictionary keys
pd.Series({2:'a', 1:'b', 3:'c'})


area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area


states = pd.DataFrame({'population': population,'area': area})
states


pop=[100,200,300]
ar=[10,20,30]
state=pd.DataFrame({'pop':pop,'ar':ar})
state

states.columns
pd.DataFrame(population,columns=['population'])


rollno=[1,2,3]
names=['a','b','c']
df=pd.DataFrame(rollno,columns=['rollnos'])
df
df['names']=names
df
df1=pd.DataFrame({'rollno':rollno,'names':names},columns=['rollno','names'])
df1
gender=['f','m','m']
df2=pd.DataFrame({'rollno':rollno,'names':names,'gender':gender},columns=['rollno','names','gender'])
df2
df3=pd.DataFrame({'rollno':rollno,'names':names,'gender':gender},columns=['rollno','names'])
df3

df4=pd.DataFrame(list(zip(rollno,names,gender)))
df4
df4.columns=['rollno','NAMES','gender']
df4


pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])


l= np.random.rand(3,2)
l
pd.DataFrame(l,columns=['foo',"bar"], index=['a','b','c'])


ind=pd.Index([2,3,5,7,11])
ind
ind[1]=0#Index is immutable
ind[::2]
ind1=pd.Index([1,3,5,7,9])
ind&ind1#intersection
ind|ind1#union

data
data.loc[2]#loc-location-explicit indexing
data.loc[2:7]

data.iloc[1:3]#iloc-index location-implicit indexing
data.iloc[0:3]

states['area']
states.area
states.population

states['density']=states.population/states.area
states
states.values[0]
states.iloc[:3,:2]
states.loc[:'Illinois',:'population']
states.ix[:3,:'area']
