# -*- coding: utf-8 -*-
"""svm implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x40fbbXz1snGtFNJZrRVeHVx8ketLaEZ

MINOR PROJECT - 4

Importing required libraries and dataset
"""

from sklearn import datasets
import matplotlib.pyplot as plt
cancer = datasets.load_breast_cancer()

"""checking the features of the given data"""

print("Features: ", cancer.feature_names)


print("Labels: ", cancer.target_names)

"""visualizing shape of the data"""

cancer.data.shape

"""printing data head"""

print(cancer.data[0:5])

"""visualizing target data"""

print(cancer.target)

"""Training and testing data"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109)

"""Importing svm and creating classifier"""

from sklearn import svm

#Create a svm Classifier
clf = svm.SVC(kernel='linear')

"""Training the model"""

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

"""printing the accuracy"""

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))