# -*- coding: utf-8 -*-
"""Jewellry- Earrings- ML model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mKbKjGhwg5Y__bOWistN11aoWAqkW2j1
"""

from random import randint
import pandas as pd
import numpy as np

import sklearn.metrics as metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("../data_synthesizer/data/dataset.csv")
X = dataset.iloc[:, 2:-1].values
y = dataset.iloc[:, 3].values

X = dataset.drop(["Unnamed: 0", "risk"], axis=1)
y = dataset["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=32
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = LogisticRegression(random_state=32, solver="liblinear")
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy score:", accuracy)
precision = metrics.precision_score(y_test, y_pred, average=None)
print("Precision score:", precision)
recall = metrics.recall_score(y_test, y_pred, average=None)
print("Recall score:", recall)

# test = sc.transform(np.array([57, 120, 1, 1, 1]).reshape(1, -1))
# print(test)
# classifier.predict_proba(test)

# dataset.head().style.background_gradient(cmap="coolwarm")

# dataset.describe().T.style.background_gradient(cmap="coolwarm")

# plt.figure(figsize=(10, 5))
# mask = np.triu(np.ones_like(dataset.corr(), dtype=bool))
# sns.heatmap(dataset.corr(), mask=mask, annot=True, cmap="Dark2")

# test = sc.transform(np.array([27, 30, 0, 0]).reshape(1, -1))
# print(test)
# classifier.predict_proba(test)

import pickle

with open("model/model.sav", "wb") as fp:
    pickle.dump(classifier, fp)
with open("model/scaler.pkl", "wb") as gp:
    pickle.dump(sc, gp)
