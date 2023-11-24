"""
This code is part of my Artificial Intelligence (CSC-462) lab coursework.
"""

#----------------Imports-----------------
import pandas as pd
import numpy as np
#----------------Imports-----------------
# Reading dataset into pandas dataframe
iris = pd.read_csv("D:\Programs\Python\Exploratory_Data_Analysis\iris.csv")
# Displaying dataset characteristics
print(iris.shape)
print(iris.describe())
print(iris.info())
print(iris.head())
print(iris.columns)
# Checking balanced and imbalanced dataset
print(iris['species'].value_counts())
# Creating separate dataframes for separate classes e.g. Setosa, Versicolor, virginica
iris_setosa = iris.loc[iris["species"]=="setosa"]
iris_setosa.describe() #describing the setosa class
iris_versicolor = iris.loc[iris["species"]=="versicolor"]
iris_versicolor.describe() #describing the versicolor class
iris_virginica = iris.loc[iris["species"]=="virginica"]
iris_virginica.describe() #describing the virginica class
# Checking central tendency measures Mean, Variance and Standard Deviation
print("Mean of Setosa Petal Length:\t", np.mean(iris_setosa["petal_length"]))
print("Mean of Setosa Petal Length with outlier:\t", np.mean(np.append(iris_setosa["petal_length"],50)))
print("Mean of Versicolor Petal Length:\t", np.mean(iris_versicolor["petal_length"]))
print("Mean of Virginca Petal Length:\t", np.mean(iris_virginica["petal_length"]))
print("Standard Deviation of Setosa Petal Length:\t", np.std(iris_setosa["petal_length"]))
print("Standard Deviation of Setosa Petal Length with outlier:\t", np.std(np.append(iris_setosa["petal_length"],50)))
print("Standard Deviation of Versicolor Petal Length:\t", np.std(iris_versicolor["petal_length"]))
print("Standard Deviation of Virginica Petal Length:\t", np.std(iris_virginica["petal_length"]))