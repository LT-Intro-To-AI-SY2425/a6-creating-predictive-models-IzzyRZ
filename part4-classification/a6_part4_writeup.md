# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer
    Unfinished
1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that? The model is far from accurate without the StandardScaler, and I think this is because the model needs a scale to regulate the independent variables with higher magnitudes. Without a scale, the data could easily be skewed based on a certain value or group of values.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain. The model is very accurate with the StandardScaler. I think this model is accurate enough for the given use case, because it gave a wrong prediction very few times.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about? The model did very well while predicting the results of the data. There was not a pattern to the inputs that the model was incorrect about.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model. 

