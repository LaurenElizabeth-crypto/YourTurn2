#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 

Location = "datasets/gradedata.xlsx"
df = pd.read_excel(Location)


# In[3]:


df.head()

