# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:54:37 2018 by Meena Sirisha"""

x1=[1,2,3]
y1=[2,4,1]
x2=[2,5,6,7,8]
y2=[5,4,8,6,1]
import matplotlib.pyplot as plt
plt.plot(x1,y1,label="line1")
plt.plot(x2,y2,label="line2")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

x1,y1
tick_label=["one","two","three"]
plt.bar(x1,y1,tick_label=tick_label,width=0.8,color=["red","green"])


marks=np.random.uniform(30,100,1000)
marks
np.all(marks >= 30)
np.all(marks < 100)
range=(20,100)
bins=10
plt.hist(marks,bins,range,color="green",histtype="bar",rwidth=0.8)

plt.scatter(x1,y1)


x1,y1
activity = ['sleep','study','eat']
colors = ['red','green','yellow']
plt.pie(y1, labels=activity, colors = colors)
plt.pie(y1, labels=activity, colors = colors, startangle=45, shadow=True, radius=1.2, explode=(0.1,0.2,0.3), autopct = '%1.1f%%')
#rotate start of pie by 90deg, explode offset each wedge, autopct - label format
plt.legend()
plt.show()


