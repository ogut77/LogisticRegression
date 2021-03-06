# -*- coding: utf-8 -*-
"""XGBoost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RrFW00FNa0fHMeoZ46yCipP6N6KB6-U1
"""

#import data
import pandas as pd
data=pd.read_excel("https://hogut.weebly.com/uploads/1/8/1/6/18163409/bookbinder2.xls")
#Let's see first five observation
print(data[:5])

#Descriptive Statistics
print(data.describe())

#Descriptive Statistcs of Categoric Variable Staus
data['Staus'].value_counts()

#Descriptive Statistcs of Categoric Variable Choice
#Choice is dependent variable
data['Choice'].value_counts()

#Descriptive Statistics of Numeric Variables
#when it is group by Choice ans Staus
data.groupby(['Choice','Staus']).mean()

data.groupby(['Choice','Staus']).count()

from sklearn import preprocessing
import numpy as np
#Convert Categoric Data to 1 if Choice==Y and Choice==N 
data['Ch']=np.where(data['Choice'] =='Y', 1,0)

data.head(5)

Training = data['Staus']=='Training'
Test = data['Staus']=='Test'
TrainingData=data[Training]
TestData=data[Test]
#Select dependent variables and independent variables for Test and Train data
X_train=TrainingData.iloc[:,:-3]
X_test=TestData.iloc[:,:-3]
y_train=TrainingData.iloc[:,-1]
y_test=TestData.iloc[:,-1]

print(y_test)

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score,confusion_matrix

model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print("Accuracy score is "+str(accuracy_score(y_test,y_pred)))