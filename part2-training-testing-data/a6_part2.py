import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values
# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size = 0.2)

# Create the model
model = LinearRegression().fit(xtrain,ytrain)
# Find the coefficient, bias, and r squared values. 
m = round(float(model.coef_[0]),2)
b = round(float(model.intercept_),2)
r_squared = model.score(xtrain,ytrain)
# Print out the linear equation and r squared value:
print(f"The line of best fit is: y = {m}x + {b}")
print(f"The r^2 value is: {r_squared}")
'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
xtest = xtest.reshape(-1,1)
# get the predicted y values for the xtest values - returns an array of the results
predictions = model.predict(xtest)
# round the value in the np array to 2 decimal places
predictions = np.around(predictions,2)
# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for i in range(len(xtest)):
    testVal = xtest[i]
    predicted_y = predictions[i]
    actual_y = ytest[i]
    print(f"X = {testVal}, Predicted Y = {predicted_y}, Actual Y = {actual_y}")
'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
plt.figure(figsize=(7,7))
plt.scatter(xtrain,ytrain,c="Red",label ="Training data")
plt.scatter(xtest,ytest,c="Blue",label="Testing data")
plt.scatter(xtest,predictions,c="Black",label ="Prediction")
plt.xlabel("Age in Years")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")
plt.plot(x,m*x+b,c="Black",label = "Line of best fit")
plt.legend()
plt.show()