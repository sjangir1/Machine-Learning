import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("TrainData.csv")
print('-----Training Dataset-----')
print(df)

regression=linear_model.LinearRegression()
regression.fit(df[['AverageValue']],df.Points)
print('')
print('Training ############################ 100%, Successful')

regression.predict([[26]])

d=pd.read_csv("TestData.csv")
print('-----Testing Dataset-----')
print(d)

test=regression.predict(d[['Averagevalue']])

d["Predicted points"]=test
print('-----Comparision table with expected and predicted points-----')
print(d)

accuracy = regression.score(d[['Averagevalue']],d[['Expected/Actual Points']])
print('Accuracy:',accuracy*100,'%')

plt.plot(d['Expected/Actual Points'],'*',
        d['Predicted points'],'.')
plt.show()    # Orange dots are the Predicted Points and Blue Stars are the Expected/Actual Points










