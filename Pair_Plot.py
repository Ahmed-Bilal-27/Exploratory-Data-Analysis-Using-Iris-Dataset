# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 01:16:39 2023

@author: RaheelShafi
"""

#----------------Imports-----------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
#----------------Imports-----------------
iris = pd.read_csv("D:\Programs\Python\Exploratory_Data_Analysis\iris.csv")
print(iris.shape)
print(iris.describe())
print(iris.info())
print(iris.head())
print(iris.columns)
print(iris['species'].value_counts())
sns.set_style('whitegrid')
sns.pairplot(iris, hue='species', size=3)
plt.show()