#!/usr/bin/env python
# coding: utf-8

# # Import Tools

# In[25]:


import pandas as pd
import matplotlib.pyplot as plt


# # Formatting Covid-19 Case Data

# In[26]:


case_data = pd.read_csv('BCCDC_COVID19_Dashboard_Case_Details.csv')


# In[27]:


# Just for showing the dataframe "case_data", no actual meaning
pd.read_csv('BCCDC_COVID19_Dashboard_Case_Details.csv')


# In[28]:


oct_data = case_data[(case_data['Reported_Date'] >= '2020-10-01') & (case_data['Reported_Date'] <= '2020-10-31')]


# In[29]:


# Just for showing the dataframe "oct_data", no actual meaning
case_data[(case_data['Reported_Date'] >= '2020-10-01') & (case_data['Reported_Date'] <= '2020-10-31')]


# In[30]:


oct_frequencies = oct_data['Reported_Date'].value_counts().rename_axis('Date').reset_index(name = 'Case Number')


# In[31]:


# Just for showing the dataframe "oct_frequencies", no actual meaning
oct_data['Reported_Date'].value_counts().rename_axis('Date').reset_index(name = 'Case Number')


# In[32]:


# Sorting the oct_frequencies dataframe by ascending date
oct_frequencies = oct_frequencies.sort_values(by='Date')


# # Plot Oct Case Number vs Date

# In[33]:


# Plot Oct case number vs date
oct_frequencies.plot(x='Date', y='Case Number', kind= 'line')

