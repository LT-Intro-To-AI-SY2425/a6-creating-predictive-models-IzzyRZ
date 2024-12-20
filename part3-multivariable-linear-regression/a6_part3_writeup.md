# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer
Unfinished
1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data? 
I got 0.86, which means that this model is fairly accurate.
2. Is your model accurate? Why or why not? This model has some pretty severe mismatches between predicted and actual values sometimes (even a negative value for one), which may mean that there are factors it is not considering that affect price.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles? 

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening? I think this is happening because it noticed that as age and mileage increase, price tends to decrease, so extrapolating that out to extremely high values produces a negative result.