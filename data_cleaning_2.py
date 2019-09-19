#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('weather.csv')
df.head(3)


# In[8]:


df = pd.melt(df,id_vars = ['id','year','month','element'],var_name = 'days',value_name = 'temp')
df.head()


# In[ ]:


df = df.pivot_table(index = ['id','year','month'],columns = ['element'],values = 'temp')


# In[14]:


df


# In[15]:


df.shape


# In[19]:


df = df.reset_index()
df


# In[20]:


df = df.drop_duplicates()
df

