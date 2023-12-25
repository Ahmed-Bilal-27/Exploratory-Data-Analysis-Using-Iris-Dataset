"""
This code is part of my Artificial Intelligence (CSC-462) lab coursework.
"""

#----------------Imports-----------------
import pandas as pd # URL: https://pandas.pydata.org/
import seaborn as sns # URL: https://seaborn.pydata.org/
import matplotlib.pyplot as plt # URL: https://matplotlib.org/
#----------------Imports-----------------
# Reading dataset into pandas dataframe
iris = pd.read_csv("D:\\Programs\\Python\\Exploratory_Data_Analysis\\iris.csv")
# Displaying dataset characteristics
print(iris.shape)
print(iris.describe())
print(iris.info())
print(iris.head())
print(iris.columns)
# Checking whether the dataset is balanced or imbalanced
print(iris['species'].value_counts())
# Creating Box Plots
"""
data=iris - It is the data to create plot of.
x='species' - iris['species'] is the x-axis.
y='petal_length' - iris['petal_length'] is the y-axis.
"""
sns.boxplot(data=iris, x='species', y='petal_length')
plt.show() # Displaying the plot