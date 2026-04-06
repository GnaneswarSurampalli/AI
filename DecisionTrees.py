import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import dtreeviz
import matplotlib.pyplot as plt
data = load_iris()
X = data.data
y = data.target

species_names = ['setosa', 'versicolor', 'virginica']
y_labels = [species_names[label] for label in y]

print("Class Labels:", y_labels)

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = y_labels
print(df.head())

setosa_data = df[df['target'] == 'setosa']
print(setosa_data.head(3))

versicolor_data = df[df['target'] == 'versicolor']
print(versicolor_data.head(3))

virginica_data = df[df['target'] == 'virginica']
print(virginica_data.head(3))

y_binary = (y == 2).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.3)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

m = dtreeviz.model(clf, X_train, y_train,
                  target_name='target',
                  feature_names=data.feature_names,
                  class_names=['virginica', 'versicolor'])

m.view()
