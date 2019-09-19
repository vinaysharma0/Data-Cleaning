#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('billboard.csv')
df.head(3)


# In[3]:


df.columns


# In[4]:


df.values


# In[5]:


df.index


# In[7]:


df.shape


# In[9]:


pd.melt(df,id_vars = ['year','artist','track','time','date.entered'],var_name = 'week')


# In[10]:


'date.entered'.split('.')

