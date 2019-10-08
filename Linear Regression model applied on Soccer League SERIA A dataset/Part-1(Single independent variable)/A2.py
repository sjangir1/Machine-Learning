import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df=pd.read_csv('S:/AML/AML-Assignment-2/Part-1/Dataset.csv')
df

X=df[['AverageValue']]
y=df['Points']

regression=linear_model.LinearRegression()

i=0
for i in range(0,20):
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.5)
    regression.fit(X_train,y_train)
    t=regression.predict(X_test)
    print(X_test)
    print(t)
    i+=1

d=pd.read_csv('dataset20experiment.csv')
points=d['Points']
predicted=d['Predicted Points']

accuracy = regression.score(df[['AverageValue']],points)
print('Accuracy:',accuracy*100,'%')

plt.plot(points,'*',
        predicted,'.')
plt.show()    # Orange dots are the Predicted Points and Blue Stars are the Expected/Actual Points

