#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[10]:


df = pd.DataFrame(np.random.randn(6,2),hier_index,columns=['A','B'])
df


# In[12]:


df.loc['G1'].loc[1]


# In[14]:


df.index.names=['Groups','Num']


# In[15]:


df


# In[18]:


df.loc['G2'].loc[2]['B']


# In[22]:


df.xs(1,level='Num')


# In[ ]:




