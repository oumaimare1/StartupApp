# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#  pickle helps perform serialization and deserialization
import pickle


# Importing the dataset
dataset = pd.read_csv('50_Startup.csv')

# The dataset contains the following features(independent variables):--
# 1) R&D Spend-Total amount of money spent on Research and Development by the startup.
# 2) Administration-Total amount of money spent on Administration by the startup.
# 3) Marketing Spend-Total amount of money spent on Marketing by the startup.
# 4) State-The State or region in which the startup is launched or operates.
X = dataset.iloc[:, :-1].values
# The dependent variable Profit which tells you the Profit acquired by the Startup.
y = dataset.iloc[:, 3].values


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Importing the Linear Regression Class
from sklearn.linear_model import LinearRegression

#Creating an object of the Linear Regression Class
regressor = LinearRegression()

#Fit the created object to our training set
regressor.fit(X, y)


# Saving model to disk
pickle.dump(regressor, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[16000, 135000, 450000]]))
