#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from numpy.random import randn


# In[3]:


np.random.seed(100)


# In[5]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[6]:


df


# In[7]:


df['W']


# In[8]:


type(df['W'])


# In[9]:


df.W


# In[10]:


df[['W','Z']]


# In[14]:


df['new']=df['W']+df['Y']


# In[15]:


df


# In[17]:


df.drop('new', axis=1, inplace=True)


# In[18]:


df


# In[19]:


df.shape


# In[20]:


df[['Z','X']]


# In[21]:


df


# In[22]:


df.loc['A']


# In[23]:


df.iloc[2]


# In[24]:


df.loc['B','Y']


# In[25]:


df.loc[['A','B'],['W','Y']]


# In[26]:


df > 0


# In[27]:


booldf =df >0
df[booldf]


# In[28]:


df['W']>0


# In[29]:


df[df['W']>0]


# In[30]:


df[df['Z']<0]


# In[31]:


df[df['W']>0]['X']


# In[32]:


df[df['W']>0][['Y','X']]


# In[39]:


boolser =df['W']>0
result=df[boolser]
mycols=['Y','Z']
result[mycols]


# In[36]:


result


# In[40]:


df[(df['W'] > 0) & (df['Y'] >1)]


# In[42]:


df.reset_index()


# In[43]:


newind='ca ny wy or co'.split()


# In[44]:


newind


# In[45]:


df['states']=newind


# In[46]:


df


# In[47]:


df.set_index('states')


# In[ ]:




