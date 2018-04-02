# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:08:17 2018 by Meena Sirisha"""

#%% Data Creation----
import numpy as np
rollnosL=[101,102,103,104,105,106,107,108,109,110,111]
namesL=["meena","apoorva","kaustav","shubham","goldie","hitesh","shruti","vijay","lalit","achal","varun"]
genderL=['F','F','M','M','M','M','F','M','M','M','M']
pythonL=np.random.randint(60,90,11)
sasL=np.random.randint(60,90,11)
import pandas as pd
series=pd.Series(namesL,index=rollnosL)
type(series)
series.index=rollnosL
series
111 in series
112 in series
print(series.index)
print(series.iteritems)
series.keys()
series.values
series.iteritems
list(series.items())
list(series.items())[1:5]
series[110]="achal kumar"
series
series=="shruti"
series[:5]
series[101:105]
series.iloc[0:5]
series.iloc[0]##implicit indexing
series.loc[101]##explicit indexing
series[0:1]
series.loc[103:110]
series.ix[108]

rollno=pd.Series(rollnosL)
gender=pd.Series(genderL)
python=pd.Series(pythonL)
sas=pd.Series(sasL)
name=pd.Series(namesL)



df=pd.concat([name,gender,python,sas],axis=1)
df
df.index=rollno
df
df.columns=("name","gender","python","sas")
df

df1=pd.DataFrame({'rollno':rollnosL,'name':namesL,'gender':genderL,'python':pythonL,'sas':sasL})
df1
df1.index=rollno
df1

df2=pd.DataFrame({'rollno':rollnosL,'name':namesL,'gender':genderL,'python':pythonL,'sas':sasL},columns=['rollno','name','gender','python','sas'])
df2
df2.index=rollno
df2
df2.transpose()
df2.T
df2.loc[101]
df2.values[0]
df2.iloc[0:1]
df2.name
df2[0:3]
df2.iloc[0:3,0:2]
df2.loc[101:105,:"python"]
df2.iloc[0:5,0:2]
df2['total']=df2['python']+df2['sas']
df2
df2[df2['total']>150]
hadoopL=np.random.randint(70,90,11)
feesL=np.random.randint(100000,150000,11)
courseL=["pg","pg","msc","msc","pg","pg","pg","pg","pg","pg","bsc"]
hadoopL=np.random.randint(60,90,11)
hostelL=[True,False,True,False,False,False,False,True,True,True,False]
df2