# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:02:04 2018 by Meena Sirisha """




import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()