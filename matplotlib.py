# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:55:52 2018 by Meena Sirisha """
#importong matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt  #this is used most often

#aesthetics style like aes in ggplot
plt.style.use('classic')
#%%plots

#plotting from script
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()
