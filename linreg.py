import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.array([[0,1],[5,1],[15,2],[25,5],[35,11],[45,15]])
y = np.array([15,11,2,8,25,32])
x2 = np.array([7,17,27,37,47,57]).reshape(-1,1)
# y2 = np.array([7,14,22,37,19,40])
# model = LinearRegression().fit(x,y)
# model.fit(x2,y2)
#print(model.intercept_, model.coef_)
#y_pred = model.predict(x)
#y_pred = model.intercept_ + model.coef_*x
#print(y_pred)
# print(model.intercept_, model.coef_)
# print(model.score)
# x_new = np.arange(5).reshape(-1,1)
# y_new = model.predict(x_new)
# print(y_new)
x_ = PolynomialFeatures(degree=2,include_bias=False).fit_transform(x)
x_2 = PolynomialFeatures(degree=2,include_bias=False).fit_transform(x2)
# trans.fit(x)
# x_ = trans.fit(x)
model = LinearRegression().fit(x_,y)
print(model.score(x_,y))
print(model.intercept_, model.coef_)
print(model.predict(x_))
print(x_)


