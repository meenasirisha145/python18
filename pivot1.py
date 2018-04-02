# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:40:36 2018 by Meena Sirisha"""

import numpy as np
import pandas as pd
data=pd.read_csv("F:\pywork\pyWork\pyProjects\mspython18/student.csv",header=0)
data
data.head()
data.columns
data.dtypes
data.select_dtypes(['object'])#only string
data['rollno'].dtype
del data['Unnamed: 0']
#data.drop(labels="Unnamed: 0",axis=1,inplace=True)
data.head()
data.describe()

data.groupby('course')['sclass'].describe()
data.groupby('course')['sclass'].describe().unstack()
data.groupby('sclass')#nothing
data.groupby('sclass').aggregate([min,np.median,max])
data[['sclass','python','sas']].groupby('sclass').aggregate([min,np.median,max,np.sum,np.std])
data[['python']]
data[['course','hadoop','sas']].groupby('course').aggregate([np.mean,np.median,min,max])
pd.pivot_table(data,index="course",values=["sas","hadoop"],aggfunc=[np.mean,np.median,min,max])
pd.pivot_table(data,index=["course","gender"],values=["sas","hadoop"],aggfunc=[np.mean,np.median,min,max])

pd.pivot_table(data,index="gender",columns="sclass",values='sas').plot(kind="bar")

aggregation={'sas':{'totalsas':'sum','avgsas':'mean'},'hadoop':{'meanhadoop':'mean','stdhadoop':'std'}}
data[data['sclass']=='C1'].groupby('gender').agg(aggregation)
data.groupby(['gender','sclass']).agg({'python':[min,max,np.mean]})

