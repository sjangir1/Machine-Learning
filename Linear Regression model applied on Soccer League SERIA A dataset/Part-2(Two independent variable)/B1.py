import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("TrainData.csv")
print("-----Training Dataset-----")
print(df)

regression=linear_model.LinearRegression()
regression.fit(df[['AverageAge','Foreigners']],df.Points)
print('')
print('Training ####################### 100%, Successful')

d=pd.read_csv("TestData.csv")
print('-----Testing Dataset-----')
print(d)

test=regression.predict(d[['AverageAge','Foreigners']])

d["Predicted points"]=test
print("-----Predicted Result-----")
print(d)

accuracy = regression.score(d[['AverageAge','Foreigners']],d[['Actual Points']])
print(accuracy*100,'%')

plt.plot(d['Actual Points'],'*',
        d['Predicted points'],'.')
plt.show()






