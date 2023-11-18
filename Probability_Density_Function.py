# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 00:29:37 2023

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
#PDF w.r.t sepal_length
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'sepal_length')\
    .add_legend()
plt.show()
#PDF w.r.t sepal_width
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'sepal_width')\
    .add_legend()
plt.show()
#PDF w.r.t petal_length
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'petal_length')\
    .add_legend()
plt.show()
#PDF w.r.t petal_width
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'petal_width')\
    .add_legend()
plt.show()