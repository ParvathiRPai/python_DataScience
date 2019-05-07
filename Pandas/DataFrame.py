#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[2]:


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df['col2'].unique()


# In[6]:


df['col2'].value_counts()


# In[8]:


df[df['col1']>2]


# In[10]:


def times(x):
    return x*2


# In[11]:


df['col1'].apply(times)


# In[12]:


df['col3'].apply(len)


# In[13]:


df['col2'].apply(lambda x:x*2)


# In[16]:


df.drop('col1', axis=1)


# In[17]:


df.columns


# In[18]:


df.index


# In[19]:


df.sort_values(by='col2')


# In[20]:


df.isnull()


# In[23]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[24]:


df


# In[25]:


df.pivot_table(values='D',index=['A','B'],columns=['C'])


# In[ ]:




