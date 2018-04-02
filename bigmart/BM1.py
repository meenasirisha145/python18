import numpy as np
import pandas as pd
import csv
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
train = pd.read_csv('train.csv')
train.isnull().sum()
w = train.loc[train.Item_Weight.isnull(),'Item_Identifier']
train.loc[train.Item_Weight.isnull(),'Item_Weight'] = [train.loc[train.Item_Identifier==w.values[i],'Item_Weight'].median() for i in range(len(w))]
train.loc[train.Item_Weight.isnull(),'Item_Weight'] = train.loc[:,'Item_Weight'].median()
z = train.loc[train.Outlet_Size.isnull(),'Outlet_Type']
train.loc[train.Outlet_Size.isnull(),'Outlet_Size'] = [train.loc[train.Outlet_Type==z.values[i],'Outlet_Size'].mode()[0] for i in range(len(z))]
dict1 = dict(zip(list(train.Item_Identifier.unique()),range(len(list(train.Item_Identifier.unique())))))
dict2 = dict(zip(list(train.Item_Fat_Content.unique()),range(len(list(train.Item_Fat_Content.unique())))))
dict3 = dict(zip(list(train.Item_Type.unique()),range(len(list(train.Item_Type.unique())))))
dict4 = dict(zip(list(train.Outlet_Identifier.unique()),range(len(list(train.Outlet_Identifier.unique())))))
dict5 = dict(zip(list(train.Outlet_Size.unique()),range(len(list(train.Outlet_Size.unique())))))
dict6 = dict(zip(list(train.Outlet_Location_Type.unique()),range(len(list(train.Outlet_Location_Type.unique())))))
dict7 = dict(zip(list(train.Outlet_Type.unique()),range(len(list(train.Outlet_Type.unique())))))
train.loc[:,'Item_Identifier'] = [dict1[train.Item_Identifier.values[i]] for i in range(len(train))]
train.loc[:,'Item_Fat_Content'] = [dict2[train.Item_Fat_Content.values[i]] for i in range(len(train))]
train.loc[:,'Item_Type'] = [dict3[train.Item_Type.values[i]] for i in range(len(train))]
train.loc[:,'Outlet_Identifier'] = [dict4[train.Outlet_Identifier.values[i]] for i in range(len(train))]
train.loc[:,'Outlet_Size'] = [dict5[train.Outlet_Size.values[i]] for i in range(len(train))]
train.loc[:,'Outlet_Location_Type'] = [dict6[train.Outlet_Location_Type.values[i]] for i in range(len(train))]
train.loc[:,'Outlet_Type'] = [dict7[train.Outlet_Type.values[i]] for i in range(len(train))]
target = train.Item_Outlet_Sales
train = train.drop(['Item_Outlet_Sales'],axis=1)
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
