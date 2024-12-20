import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values


#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25)
#create linear regression model
model = LinearRegression().fit(xtrain,ytrain)
prediction = model.predict(xtest)
prediction = np.around(prediction,2)
#Find and print the coefficients, intercept, and r squared values.
#Each should be rounded to two decimal places. 
coefficients = np.around(model.coef_,2)
intercept = round(float(model.intercept_),2)
r_squared = round(model.score(x,y),2)
print(f"Model equation: y = {coefficients[0]}x1 + {coefficients[1]}x2 + {intercept}")
print(f"R squared value: {r_squared}")
#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")
for i in range(len(xtest)):
    print(f"Miles: {xtest[i][0]} Age: {xtest[i][1]} Predicted price: {prediction[i]} Actual price: {ytest[i]}")