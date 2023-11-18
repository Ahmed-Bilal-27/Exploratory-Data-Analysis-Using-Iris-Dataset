"""
This code is part of my Artificial Intelligence (CSC-462) lab coursework.
"""

#----------------Imports-----------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
#----------------Imports-----------------
# Reading dataset into pandas dataframe
iris = pd.read_csv("iris.csv")
# Displaying dataset characteristics
print(iris.shape)
print(iris.describe())
print(iris.info())
print(iris.head())
print(iris.columns)
# Checking balanced and imbalanced dataset
print(iris['species'].value_counts())
# Distribution Plot w.r.t sepal_length
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'sepal_length')\
    .add_legend()
plt.show()
# Distribution Plot w.r.t sepal_width
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'sepal_width')\
    .add_legend()
plt.show()
# Distribution Plot w.r.t petal_length
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'petal_length')\
    .add_legend()
plt.show()
#Distribution Plot w.r.t petal_width
sns.FacetGrid(iris, hue='species', height=4)\
    .map(sns.distplot, 'petal_width')\
    .add_legend()
plt.show()