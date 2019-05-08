#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')
tips.head()


# In[3]:


import numpy as np


# In[4]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[6]:


sns.countplot(x='sex',data=tips)


# In[9]:


sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')


# In[10]:


sns.violinplot(x='day', y='total_bill', data=tips)


# In[12]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)


# In[13]:


sns.swarmplot(x='day', y='total_bill', data=tips)


# In[14]:


sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')


# In[17]:


sns.factorplot(x='day', y='total_bill', data=tips,  kind='violin')


# In[ ]:




