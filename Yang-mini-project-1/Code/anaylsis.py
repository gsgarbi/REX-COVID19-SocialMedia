#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt


# In[19]:


df = pd.read_csv('COVID_by_day.csv')

df.head()


# In[20]:


X = df['Date']
Y = df['New_reported_cases']


# In[21]:


plt.plot(X,Y)


# In[ ]:




