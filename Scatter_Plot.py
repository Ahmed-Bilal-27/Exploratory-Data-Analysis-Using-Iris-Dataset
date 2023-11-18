# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 05:52:30 2023

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
iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show()
sns.set_style('whitegrid')
sns.FacetGrid(iris, hue='species', height=4)\
    .map(plt.scatter, 'sepal_length', 'sepal_width')\
    .add_legend()
plt.show()