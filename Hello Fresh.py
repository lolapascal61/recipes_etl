#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import json


# In[26]:


#Import recipes
recipes = pd.read_json('recipes.json', lines=True)
recipes.head()


# In[90]:


#Extract every recipe containing chillies 
recipes_chilli = recipes[(recipes['ingredients'].str.contains('Chilies')) | (recipes['ingredients'].str.contains('Chili')) |
       (recipes['ingredients'].str.contains('Chiles')) | (recipes['ingredients'].str.contains('Chillies')) |
                        (recipes['ingredients'].str.contains('Chilie')) | (recipes['ingredients'].str.contains('Chile')) |
                         (recipes['ingredients'].str.contains('Chillie'))]
recipes_chilli.head()


# In[66]:


#Convert cookTime and prepTime into correct format
import isodate

recipes_chilli['cookTime_time'] = 0
recipes_chilli['prepTime_time'] = 0
for i in range(len(recipes_chilli)):
    recipes_chilli['cookTime_time'].iloc[i] = isodate.parse_duration(recipes_chilli['cookTime'].iloc[i])
    recipes_chilli['prepTime_time'].iloc[i] = isodate.parse_duration(recipes_chilli['prepTime'].iloc[i])
    
#Sum cooking and preparation time
recipes_chilli['total_time'] = recipes_chilli['cookTime_time'] + recipes_chilli['prepTime_time']


# In[84]:


#Create difficulty variable
import numpy as np

#List of conditions
conditions = [
    (recipes_chilli['total_time'] > '01:00:00'),
    (('01:00:00' >= recipes_chilli['total_time']) & ( recipes_chilli['total_time'] >= '00:30:00')),
    ((recipes_chilli['total_time'] < '00:30:00'))
    ]

#List of the values we want to assign for each condition
values = ['Hard', 'Medium', 'Easy']

#Create a new column for difficulty
recipes_chilli['difficulty'] = np.select(conditions, values)

recipes_chilli['difficulty'].fillna('Unknown', inplace = True)
recipes_chilli.head()


# In[85]:

#Save as csv file
recipes_chilli.to_csv('recipes_chilli.csv', header= True, index=False)

