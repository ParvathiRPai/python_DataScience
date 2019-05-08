#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np


# In[4]:


x=np.linspace(0,5,11)


# In[5]:


y=x**2


# In[9]:


plt.plot(x,y,'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title("Title")


# In[13]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[17]:


fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X label')


# In[21]:





# In[31]:


fig,axes=plt.subplots(nrows=1,ncols=2)
for current_ax in axes:
    current_ax.plot(x,y)
    
plt.tight_layout()


# In[30]:


axes[0].plot(x,y)


# In[33]:


fig=plt.figure(figsize=(8,2))
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[37]:


fig,axes=plt.subplots(nrows=2, ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(x,y)


# In[40]:


fig.savefig('my_picture.jpg',dpi=200)


# In[45]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label= 'x square')
ax.plot(x,x*3, label= 'x cubed')
ax.legend(loc=10)


# In[56]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',linewidth=3,alpha=0.5,linestyle='--', marker='o', markersize=20, markerfacecolor='pink')
ax.set_xlim([0,1])
ax.set_ylim([0,2])


# In[ ]:




