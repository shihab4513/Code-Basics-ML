#given Canada's adjusted net national income per capita. you want to predict net income in year 2020
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv('canada_per_capita_income.csv')
#print(df)
plt.xlabel('year')
plt.ylabel('Per capita income (US$)')
plt.scatter(df['year'], df['per_capita_income_usd'])
reg=linear_model.LinearRegression()
reg.fit(df[['year']], df.per_capita_income_usd)
plt.plot(df[['year']], reg.predict(df[['year']]))
plt.show()
x=2018
prediction=reg.predict([[x]])
print("Predicted price is ${}".format(prediction))