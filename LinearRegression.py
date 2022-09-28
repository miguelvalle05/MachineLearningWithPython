import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df= pd.read_csv("FuelConsumptionCo2.csv")


# take a look at the dataset
print(df.head())

# summarize the data
print(df.describe())

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(9))


viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()
