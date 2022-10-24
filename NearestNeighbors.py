import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing

df = pd.read_csv('teleCust1000t.csv')
print(df.head())

print(df['custcat'].value_counts())

df.hist(column='income', bins=50)


X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
X[0:5]



y = df['custcat'].values
y[0:5]

#nomalize data
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X[0:5]