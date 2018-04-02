# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:43:36 2018 by Meena Sirisha"""
import numpy as np
import pandas as pd
rollnosL=[101,102,103,104,105,106,107,108,109,110,111]
namesL=["meena","apoorva","kaustav","shubham","goldie","hitesh","shruti","vijay","lalit","achal","varun"]
genderL=['F','F','M','M','M','M','F','M','M','M','M']
pythonL=np.random.randint(60,90,11)
sasL=np.random.randint(60,90,11)

hadoopL=np.random.randint(70,90,11)
feesL=np.random.randint(100000,150000,11)
courseL=["pg","pg","msc","msc","pg","pg","pg","pg","pg","pg","bsc"]
hadoopL=np.random.randint(60,90,11)
hostelL=[True,False,True,False,False,False,False,True,True,True,False]

df=pd.DataFrame({'rollno':rollnosL,'name':namesL,'gender':genderL,'hostel':hostelL,'python':pythonL,'sas':sasL,'hadoop':hadoopL,'course':courseL,'fees':feesL},columns=['rollno','name','gender','hostel','python','sas','hadoop','course','fees'])
df
df['total']=df['python']+df['sas']+df['hadoop']
df
df.to_csv("student.csv")
df.columns
df.groupby('gender').mean()
df.groupby('gender').size()
df.groupby('gender').sum()
from numpy import random
classes=['C1','C2','C3']
sclass = random.choice(classes,11)
sclass
df['sclass']=pd.Series(sclass)
df
pd.pivot_table(df,index=['name'])
pd.pivot_table(df,index=['name','sclass'])
pd.pivot_table(df,index=['name','sclass','hostel'])
pd.pivot_table(df,index=['course','sclass',],values=['total','python'])#default is mean
pd.pivot_table(df,index=['course','sclass',],values=['total','python'],aggfunc=np.sum)
pd.pivot_table(df,index=['course','sclass',],values=['total','python'],aggfunc=[np.sum,np.mean,len])
