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
# Making Scatter Plot the sepal_length and sepal_width features
iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show()
sns.set_style('whitegrid')
sns.FacetGrid(iris, hue='species', height=4)\
    .map(plt.scatter, 'sepal_length', 'sepal_width')\
    .add_legend()
plt.show()