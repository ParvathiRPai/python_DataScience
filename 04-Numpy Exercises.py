

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


np.zeros(10)


# #### Create an array of 10 ones

# In[3]:


np.ones(10)


# #### Create an array of 10 fives

# In[5]:


np.ones(10)*5


# #### Create an array of the integers from 10 to 50

# In[7]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[8]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[10]:


np.arange(0,9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[12]:


np.identity(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[24]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[22]:


np.random.randn(25)


# #### Create the following matrix:

# In[27]:


np.arange(1,101).reshape(10,10)/10


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[28]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[33]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[37]:


mat[2:,1:]


# In[40]:





# In[38]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3,4]


# In[41]:





# In[41]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[0:3,1:2]


# In[42]:





# In[43]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[4:,:]


# In[46]:





# In[44]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3:,:]


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[45]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[46]:


mat.std()


# #### Get the sum of all the columns in mat

# In[47]:


mat.sum(axis=0)


# # Great Job!
