#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


pd.read_csv('example')


# In[5]:


df=pd.read_csv('example')


# In[6]:


df.to_csv('My_output',index=False)


# In[7]:


pd.read_csv('My_output')


# In[ ]:


conda install xlrd


# In[ ]:


df=pd.read_excel('Excel_sample.xlsx',sheetname='Sheet1')


# In[17]:


df


# In[19]:


df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')


# In[21]:


conda install lxml


# In[ ]:


conda install html5lib


# In[ ]:


conda install BeautifulSoup4


# In[ ]:


df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# In[31]:





# In[ ]:




