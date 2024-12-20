# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model? 
I got an r^2 value of 0.6257932855322312, which makes sense, considering that the data points were pretty far from the line of best fit on the graph. This r^2 value shows that there is a significant correlation, but not a particularly strong one.
2. According to your model, what is the predicted systolic blood pressure for a person who is 43 years old? 
The predicted blood pressue for x=43 was 137.46185286
3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?
The model's predictions definitely look like they would make sense, but they are nowhere near accurate enough to reliably predict blood pressure, considering the middling r^2 value. A larger data pool would probably improve its accuracy.