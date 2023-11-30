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
# Checking measures Median, Quantile and Percentile
print("Median of Setosa Petal Length:\t", np.median(iris_setosa["petal_length"]))
print("Median of Setosa Petal Length with outlier:\t", np.median(np.append(iris_setosa["petal_length"],50)))
print("Median of Versicolor Petal Length:\t", np.median(iris_versicolor["petal_length"]))
print("Median of Virginca Petal Length:\t", np.median(iris_virginica["petal_length"]))
print("Quantiles of Setosa Petal Length:\t", np.percentile(iris_setosa["petal_length"], np.arange(0, 125, 25)))
print("Quantiles of Versicolor Petal Length:\t", np.percentile(iris_versicolor["petal_length"], np.arange(0, 125, 25)))
print("Quantiles of Virginca Petal Length:\t", np.percentile(iris_virginica["petal_length"], np.arange(0, 125, 25)))
print("90th percentile of Setosa Petal Length:\t", np.percentile(iris_setosa["petal_length"], 90))
print("90th percentile of Versicolor Petal Length:\t", np.percentile(iris_versicolor["petal_length"], 90))
print("90th percentile of Virginca Petal Length:\t", np.percentile(iris_virginica["petal_length"], 90))
