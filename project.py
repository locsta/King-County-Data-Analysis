#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
kc_clean = pd.read_csv('clean_data.csv')
kc=pd.read_csv('kc_house_data.csv')


# In[2]:


from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm_no_grade = LinearRegression()

# X contaning the 3 features
X = kc_clean[['grade', 'sqft_living', 'zip_mean_price']]

# X contaning the only the sqft_living and zip_mean_price features
X_no_grade = kc_clean[['sqft_living', 'zip_mean_price']]

y = kc_clean['log_price']
lm.fit(X,y)
lm_no_grade.fit(X_no_grade,y)


# In[3]:


zipcodes = kc["zipcode"].unique()
zipcodes_dict = {}
for zipcode in zipcodes:
    mean = kc.loc[kc["zipcode"] == zipcode, "price"].mean()
    if mean <= 300000:
        zipcodes_dict[zipcode] = 0
    elif mean > 300000 and mean <= 500000:
        zipcodes_dict[zipcode] = 1
    elif mean > 500000 and mean <= 700000:
        zipcodes_dict[zipcode] = 2
    else:
        zipcodes_dict[zipcode] = 3

def predict(sqft_living,zipcode,grade=None):
    zipcode = zipcodes_dict[zipcode]
    if grade is None:
        data = pd.DataFrame([{'sqft_living': sqft_living, 'zip_mean_price':zipcode}])
        pred = lm_no_grade.predict(data)
    else:
        if grade <= 5:
            grade = 0
        elif grade > 5 and grade <= 6:
            grade = 1
        elif grade > 6 and grade <= 7:
            grade = 2
        elif grade > 7 and grade <= 8:
            grade = 3
        elif grade > 8 and grade <= 9:
            grade = 4
        elif grade > 9 and grade <= 11:
            grade = 5
        else:
            grade = 6
        data = pd.DataFrame([{'grade': grade, 'sqft_living': sqft_living, 'zip_mean_price':zipcode}])
        pred = lm.predict(data)
    return print('Price: $',round(np.exp(pred)[0]))


# In[4]:


sqft_living = int(input('Enter Living Area in sqft: '))
zipcode = int(input('Enter the Zipcode: '))
grade_str = input('Enter Grade of the House: ')
grade = None if grade_str is '' else int(grade_str)
predict(sqft_living,zipcode,grade)


# In[ ]:




