# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:09:55 2020

@author: StevensUser
"""
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets



file2 = open('PAhrs.csv','r')
data2=[]

for line in file2:
    parts = line.strip().split(',')
    data2.append(parts)
    
print(len(data2[0]))
print(len(data2[1]))


xcoordinates = []
for i in range(len(data2)):
    xcoordinates.append(data2[i][37])
    
print(xcoordinates[:5])

ycoordinates = []
for i in range(len(data2)):
    ycoordinates.append(data2[i][38])
    
print(ycoordinates[:5])


import numpy as np
import matplotlib.pyplot as plt


x = xcoordinates[1:]
y = ycoordinates[1:]

plt.scatter(x, y)
plt.show()