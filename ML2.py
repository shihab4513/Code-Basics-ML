import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel('homeprices.xlsx')
print(df)

plt.xlabel('area(sqr ft)')
plt.ylabel('price(US$)')
plt.scatter(df.area, df.price, color='red', marker='+')

#plt.show()
reg = linear_model.LinearRegression()

reg.fit(df[['area']], df.price)
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
plt.show()
#y=mx+b. here coef_is m, intercept_ is b
x=1000
prediction=reg.predict([[x]])
print("Predicted price is ${}".format(prediction))
print("x =",x)
m=reg.coef_
b=reg.intercept_
print("m =",m)
print("b =",b)
y=(m*x+b)
print("y =",y)

d=pd.read_excel('areas.xlsx')
p=reg.predict(d)
d['prices']=p
print(d.head(3))
d.to_excel('prediction.xlsx', index=False)

print(p)