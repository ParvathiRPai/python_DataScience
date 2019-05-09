#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
tips = sns.load_dataset('tips')


# In[3]:


tips.head()


# In[4]:


flights.head()


# In[7]:


tc=tips.corr()


# In[14]:


sns.heatmap(tc, annot=True,cmap='coolwarm')


# In[15]:


flights.pivot_table(index='month', columns='year', values='passengers')


# In[16]:


fp=flights.pivot_table(index='month', columns='year', values='passengers')


# In[18]:


sns.heatmap(fp,cmap='magma', linecolor='white', linewidths=1)


# In[22]:


sns.clustermap(fp, cmap='coolwarm', standard_scale=1)


# In[ ]:




