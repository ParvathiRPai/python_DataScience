
# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[3]:


sal=pd.read_csv('Salaries.csv')
sal


# ** Check the head of the DataFrame. **

# In[8]:





# ** Use the .info() method to find out how many entries there are.**

# In[4]:


sal.info()


# **What is the average BasePay ?**

# In[7]:


sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[9]:


sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[20]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[21]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[23]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[26]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[29]:


sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[30]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[32]:


sal['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[35]:


sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[43]:


def cheif_string(title):
    if 'cheif' in title.lower().split():
        return True
    else:
        return False 


# In[44]:


sum(sal['JobTitle'].apply(lambda x:cheif_string(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[45]:


sal['title_len']=sal['JobTitle'].apply(len)


# In[46]:


sal[['TotalPayBenefits','title_len']].corr()


# # Great Job!
