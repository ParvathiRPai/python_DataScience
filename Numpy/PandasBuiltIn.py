#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np


# In[11]:


import seaborn as sns


# In[2]:


import pandas as pd


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df1=pd.read_csv('df1', index_col=0)


# In[5]:


df1.head()


# In[6]:


df2=pd.read_csv('df2')
df2.head()


# In[8]:


df1['A'].hist(bins=30)


# In[15]:


df1['A'].plot(kind='hist', bins=30)


# In[17]:


df2.plot.area(alpha=0.4)


# In[19]:


df2.plot.bar(stacked=True)


# In[20]:


df1['A'].plot.hist(bins=50)


# In[28]:


df1.plot.scatter(x='A', y='B', c='C',cmap='coolwarm',s=df1['C']*100)


# In[29]:


df2.plot.box()


# In[30]:


df=pd.DataFrame(np.random.randn(100,2),columns=['a','b'])


# In[34]:


df.plot.hexbin(x='a',y='b', gridsize=25)


# In[35]:


df2['a'].plot.kde()


# In[ ]:




