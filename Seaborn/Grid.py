#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


iris=sns.load_dataset('iris')


# In[4]:


iris.head()


# In[5]:


iris['species'].unique()


# In[7]:


sns.pairplot(iris)


# In[12]:


g=sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_lower(sns.kdeplot)
g.map_upper(sns.scatter)


# In[13]:


tips=sns.load_dataset('tips')


# In[14]:


tips.head()


# In[17]:


g=sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot, 'total_bill')


# In[24]:


sns.lmplot(x='total_bill', y='tip', data=tips , hue='sex', markers=['o','v'], scatter_kws={'s':100})


# In[29]:


sns.lmplot(x='total_bill', y='tip', data=tips , col='sex', row='time', hue='sex', aspect=0.6, size=8)


# In[35]:


sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)
sns.despine(left=True)


# In[40]:


sns.set_context('poster', font_scale=3)
sns.countplot(x='sex', data=tips)


# In[41]:


sns.lmplot(x='total_bill', y='tip', data=tips)


# In[ ]:




