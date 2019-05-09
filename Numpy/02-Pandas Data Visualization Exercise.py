#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Pandas Data Visualization Exercise
# 
# This is just a quick exercise for you to review the various plots we showed earlier. Use **df3** to replicate the following plots. 

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df3.info()


# In[5]:


df3.head()


# ** Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size. See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...**

# In[11]:


df3.plot.scatter(x='a', y='b',figsize=(12,3),s=50)


# ** Create a histogram of the 'a' column.**

# In[13]:


df3['a'].plot.hist(bins=20)


# ** These plots are okay, but they don't look very polished. Use style sheets to set the style to 'ggplot' and redo the histogram from above. Also figure out how to add more bins to it.***

# In[16]:


plt.style.use('ggplot')
df3['a'].plot.hist(bins=20, alpha=0.5)


# In[7]:





# ** Create a boxplot comparing the a and b columns.**

# In[17]:


df3[['a','b']].plot.box()


# ** Create a kde plot of the 'd' column **

# In[18]:


df3['d'].plot.kde()


# ** Figure out how to increase the linewidth and make the linestyle dashed. (Note: You would usually not dash a kde plot line)**

# In[20]:


df3['d'].plot.kde(lw=5, ls='--')


# ** Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).**

# In[21]:


df3.ix[0:30].plot.area()


# ## Bonus Challenge!
# Note, you may find this really hard, reference the solutions if you can't figure it out!
# ** Notice how the legend in our previous figure overlapped some of actual diagram. Can you figure out how to display the legend outside of the plot as shown below?**
# 
# ** Try searching Google for a good stackoverflow link on this topic. If you can't find it on your own - [use this one for a hint.](http://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas)**

# In[23]:


f=plt.figure()
df3.ix[0:30].plot.area()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


# # Great Job!
