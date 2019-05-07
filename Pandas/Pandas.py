#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}


# In[4]:


pd.Series(data=my_data)


# In[6]:


pd.Series(data=my_data, index=labels)


# In[7]:


pd.Series(d)


# In[8]:


pd.Series(data=[sum, print, len])


# In[9]:


ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])


# In[10]:


ser1


# In[11]:


ser1['USA']


# In[12]:


ser3=pd.Series(data=labels)


# In[18]:


ser3


# In[ ]:




