import numpy as np
import pandas as pd
import csv
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
train = pd.read_csv('bigmarttrain.csv')
train.isnull().sum()
w = train.loc[train.Item_Weight.isnull(),'Item_Identifier'].unique()
w
w.shape
list(w)
for x in list(w):
    train.loc[(train.Item_Weight.isnull()) & (train.Item_Identifier==x),'Item_Weight'] =        train.loc[train.Item_Identifier==x,'Item_Weight'].median()

for x in list(w):
    print(x)

train.isnull().sum()

train.loc[train.Item_Weight.isnull(),'Item_Weight'] = train.loc[:,'Item_Weight'].median()
z = train.loc[train.Outlet_Size.isnull(),'Outlet_Type']

for x in z:
    train.loc[(train.Outlet_Size.isnull()) & (train.Outlet_Type==x),'Outlet_Size'] = train.loc[train.Outlet_Type==x,'Outlet_Size'].mode()[0]

train.isnull().sum()

train.Item_Fat_Content=train.Item_Fat_Content.astype("category").cat.codes
train.head()

train.Outlet_Type=train.Outlet_Type.astype("category").cat.codes
train.head()

train.Outlet_Location_Type=train.Outlet_Location_Type.astype("category").cat.codes
train.head()
train.Outlet_Establishment_Year=train.Outlet_Establishment_Year.astype("category").cat.codes
train.Outlet_Size=train.Outlet_Size.astype("category").cat.codes
train.Item_Type=train.Item_Type.astype("category").cat.codes

train.head()

target = train.Item_Outlet_Sales
train = train.drop(['Item_Outlet_Sales','Item_Identifier','Outlet Identifier'],axis=1)
train1 = train[0:7600]
train2 = train[7600:]
target1 = target[0:7600]
target2 = target[7600:]
tra1 = np.array(train1)
tra2 = np.array(train2)
tar1 = np.array(target1)
tar2 = np.array(target2)
model = RandomForestRegressor(n_estimators=200,criterion='mse',max_depth=None,min_samples_split=75,min_samples_leaf=1,max_features='auto',max_leaf_nodes=None,\
min_impurity_split=1e-07,bootstrap=True,oob_score=False,n_jobs=-1,random_state=79,verbose=1,warm_start=False)
model = model.fit(tra1,tar1)
scorer = mean_squared_error(tar2,model.predict(tra2))
print(math.sqrt(scorer))
test = pd.read_csv('test.csv')
test.isnull().sum()
wt = test.loc[test.Item_Weight.isnull(),'Item_Identifier']
test.loc[test.Item_Weight.isnull(),'Item_Weight'] = [test.loc[test.Item_Identifier==wt.values[i],'Item_Weight'].median() for i in range(len(wt))]
test.loc[test.Item_Weight.isnull(),'Item_Weight'] = test.loc[:,'Item_Weight'].median()
zt = test.loc[test.Outlet_Size.isnull(),'Outlet_Type']
test.loc[test.Outlet_Size.isnull(),'Outlet_Size'] = [test.loc[test.Outlet_Type==zt.values[i],'Outlet_Size'].mode()[0] for i in range(len(zt))]
itemsid = test.Item_Identifier
storeid = test.Outlet_Identifier
test.loc[:,'Item_Identifier'] = [dict1[test.Item_Identifier.values[i]] for i in range(len(test))]
test.loc[:,'Item_Fat_Content'] = [dict2[test.Item_Fat_Content.values[i]] for i in range(len(test))]
test.loc[:,'Item_Type'] = [dict3[test.Item_Type.values[i]] for i in range(len(test))]
test.loc[:,'Outlet_Identifier'] = [dict4[test.Outlet_Identifier.values[i]] for i in range(len(test))]
test.loc[:,'Outlet_Size'] = [dict5[test.Outlet_Size.values[i]] for i in range(len(test))]
test.loc[:,'Outlet_Location_Type'] = [dict6[test.Outlet_Location_Type.values[i]] for i in range(len(test))]
test.loc[:,'Outlet_Type'] = [dict7[test.Outlet_Type.values[i]] for i in range(len(test))]
tester = np.array(test)
pred = model.predict(tester)
submission = pd.DataFrame(itemsid,columns=['Item_Identifier'])
submission['Outlet_Identifier'] = storeid
submission['Item_Outlet_Sales'] = pred
submission.to_csv('BM1.csv',index=False)
