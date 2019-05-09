#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np 


# In[16]:


pip install plotly


# In[17]:


pip install cufflinks


# In[18]:


from plotly import __version__


# In[19]:


import cufflinks as cf


# In[21]:


print(__version__)


# In[22]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[23]:


init_notebook_mode(connected=True)


# In[24]:


cf.go_offline()


# In[25]:


df=pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())


# In[26]:


df.head()


# In[29]:


df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})


# In[33]:


df.iplot()


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


df.iplot(kind='scatter',x='A',y='B', mode='markers')


# In[39]:


df2.iplot(kind='bar', x='Category', y='Values')


# In[42]:


df.count().iplot(kind='bar')


# In[44]:


df.iplot(kind='box')


# In[47]:


df3=pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10], 'z':[5,4,3,2,1]})


# In[48]:


df3.iplot(kind='surface', colorscale='rdylbu')


# In[50]:


df['A'].iplot(kind='hist', bins=50)


# In[52]:


df[['A','B']].iplot(kind='spread')


# In[53]:


df.iplot(kind='bubble',x='A',y='B',size='C')


# In[55]:


1+2


# In[ ]:




