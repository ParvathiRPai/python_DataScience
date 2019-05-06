
# In[1]:


my_list=[1,2,3]


# In[2]:


import numpy as np


# In[3]:


arr =np.array(my_list)


# In[4]:


arr


# In[5]:


my_mat=[[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


np.array(my_mat)


# In[9]:


np.arange(0,10,2)


# In[12]:


np.zeros((2,3))


# In[13]:


np.ones((2,1))


# In[14]:


np.linspace(0,5)


# In[15]:


np.eye(4)


# In[16]:


np.random.rand(5)


# In[17]:


np.random.rand(5,5)


# In[18]:


np.random.randn(2)


# In[19]:


np.random.randn(4,4)


# In[21]:


np.random.randint(1,100,10)


# In[23]:


arr=np.arange(25)


# In[24]:


arr


# In[25]:


ranarr=np.random.randint(0,50,10)


# In[26]:


ranarr


# In[27]:


arr.reshape(5,5)


# In[29]:


ranarr.max()


# In[30]:


ranarr.argmax()

arr.shape
# In[31]:


arr.shape


# In[32]:


arr.reshape(5,5)


# In[33]:


arr.dtype


# In[34]:


from numpy.random import randint


# In[35]:


randint(2,10)


# In[36]:


import numpy as np


# In[37]:


arr=np.arange(0,11)


# In[38]:


arr


# In[39]:


arr[8]


# In[40]:


arr[1:5]


# In[41]:


arr[:6]


# In[42]:


arr[5:]


# In[48]:


arr[0:5]


# In[45]:


arr


# In[47]:


slice_of_arr=arr[0:6]
slice_of_arr


# In[49]:


arr_copy=arr.copy()


# In[50]:


arr_copy


# In[54]:


arr_2d=np.array([[5,10,15],[20,25,30],[30,35,40]])


# In[55]:


arr_2d


# In[56]:


arr_2d[0][1]


# In[57]:


arr_2d[1,2]


# In[59]:


arr_2d[:2,1:]


# In[60]:


arr_2d[1:,:3]


# In[61]:


arr=np.arange(1,11)


# In[62]:


arr


# In[63]:


arr > 5


# In[64]:


arr[arr<3]


# In[65]:


arr_2d=np.arange(50).reshape(5,10)


# In[67]:


arr_2d


# In[68]:


arr_2d[3:,:4]


# In[ ]:




