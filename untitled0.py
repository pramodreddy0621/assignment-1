# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pI73fArbqbR-aNeVsIKgbjMw1ibhg1LU
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics

data = [['Dot', 1], ['Dot', 2], ['Cross', 3], ['Cross',6], ['Cross',6], ['Dot',7], ['Dot',10], ['Dot',11]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Class', 'Value'])

df.head()

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.5, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
  
knn.fit(X, y)
  
y_pred = knn.predict(X_test)

y_pred

confusion_matrix(y_test, y_pred)

Accuracy = metrics.accuracy_score(y_test, y_pred)

Accuracy