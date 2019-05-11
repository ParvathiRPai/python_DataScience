#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[3]:


init_notebook_mode(connected=True)


# In[7]:


data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})


# In[8]:


layout=dict(geo={'scope':'usa'})


# In[9]:


choromap=go.Figure(data=[data], layout=layout)


# In[11]:


iplot(choromap)


# In[12]:


import pandas as pd
df=pd.read_csv('2011_US_AGRI_Exports')


# In[13]:


df.head()


# In[26]:


data = dict(type='choropleth',
            colorscale = 'YIOrRd',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Millions USD"}
            ) 


# In[27]:


layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[29]:


choromap2 = go.Figure(data = [data],layout = layout)


# In[ ]:




