# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:45:25 2018

@author: Wasimakram
"""
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('F:/pywork/pyWork/pyProjects/mspython18/Contriesdata.csv',header=0)
#df = pd.concat([df[col].dropna().reset_index(drop=True) for col in df], axis=1)
df.head()

X = df["Agriculture"]
y = df["Literacy"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
model.summary()

##
from sklearn import linear_model

df = pd.read_csv('E:/TRN/Data 2017/Contriesdata.csv',header=0)
df = pd.concat([df[col].dropna().reset_index(drop=True) for col in df], axis=1)
df = pd.DataFrame(df)
target = pd.DataFrame(df, columns=["GDP per captia USD per annum"])
df.head()

x = df["Deathrate"]
y = target

# Note the difference in argument order
lm = linear_model.LinearRegression()
model = lm.fit(y,x) # make the predictions by the model

predictions = lm.predict(y)
print(predictions)[0:5]

# Print out the statistics
model.summary()