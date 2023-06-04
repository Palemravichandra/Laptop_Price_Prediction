# Laptop_Price_Prediction
### Importing required libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
- Reading the data
- Checking for duplicated values and null values 

### Data Cleaning
- Cleaning the Weight and Ram columns and converting to integer and float format 
- Extracting screen resolution column by using regular expressions
- Extracting cpu column

### Univariate analysis
- perform the univariate analysis i.e. how the each feature is distributed
- if any value treaten as null value replace it with mode of perticular feature

### Bivariate analysis
- Bivariate analysis is knowing how feature is distrubuted with respect totarget variable

### Encoding
- Transforming categorical features into numerical values

### Feature selection
- checking for the features for correlated or not by setting threshold value

### splitting the data
- splitting the data into train data and test data

### standerdization
- Transforming train data from range of numerical values into  between 0 to 1

### Model building
- Building the model and train with different parameters by applying different algorithems
- Selecting the model which performs well
- Saving the model
### App creation
- Creating the app using streamlit
