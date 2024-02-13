# -*- coding: utf-8 -*-
"""RedWineQuality.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vHL4zo6ITExm2h9p-7Cl4uD6DjZo_iL2
"""

import pandas as pd
import numpy as np
df=pd.read_csv('/content/winequality-red.csv')
df

df.head()

df.tail()

df.isna().sum()

df.dtypes

x=df.iloc[:,:-1].values
x

y=df.iloc[:,-1].values
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)
x_train

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x_train)
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)
x_test

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='entropy')
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score,confusion_matrix
print('Accuracy score',accuracy_score(y_test,y_pred))
print('Confusion matrix',confusion_matrix(y_test,y_pred))

df.dtypes

from sklearn import tree
import matplotlib.pyplot as plt
plt.figure(figsize=(15,15))
tree.plot_tree(dt,feature_names=['fixed acidity','fixed acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol'],filled=True)