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
# Pair Plotting the dataset features
sns.set_style('whitegrid')
sns.pairplot(iris, hue='species', size=3)
plt.show()