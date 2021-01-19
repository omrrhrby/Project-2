#!/usr/bin/env python
# coding: utf-8

# 
# # Project: Investigate a Dataset (TMDB-Movies)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# > In this project, I will ba analyzing a dataset of 10,000 movies obtained from The Movie Database (TMDb). By using Python and python' libraries Numby, Pandas and Mayplotlip 
# 
# > **Qustions:**
# 
# - What kinds of properties are associated with movies that have high revenues?
# 
# - which year has the most number of film produced?
# 
# - Highest film in terms of profits and lowest?
# 
# 
# >
# 

# In[1]:


#First call the neccessery library to analyse the data 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.
# 
# ### General Properties

# In[2]:


#Display the set
omv_df = pd.read_csv('tmdb-movies.csv')
omv_df.head(2)


# In[3]:


#overview of the dtat set
omv_df.info()


# In[4]:


omv_df.shape


# In[5]:


#overview of the statistics
omv_df.describe()


# In[6]:


#Check if there is any null data and  
omv_df.isna().sum()


# In[7]:


#Check duplicate!
omv_df.duplicated()

sum(omv_df.duplicated())


# > **observation**: 
# observation of the original dataset:
# - there are 21 clomuns and 10866 entries in the set
# - missing data in clomuns:(imdb_id, cast, homepage, director, tagline, keywords, overviews, genres, production_companies).
# - Null data in clomuns: ( imdb_id, cast, homepage, dierctor, tagline, keywords, overview, genres, production_companies).
# - (relesa_date) datatype is an object insted of date type. 
# - there is 1 dublicate data in the set.
# - revenue and budget have 0 value in the thier rows
# - cast has multible  entries in each cell
# 
# 
# 
# ### Data Cleaning 
# 
# > To Do
# - Drop uncessery cloumn 
# - Remove Dublicate
# - drop Null values
# - replace missing data or 0 with mean 
# 
# 

# In[8]:


#drop cloumns wont be helpful for answering the qustions and analysing the data
omv_df.drop(['id','imdb_id','homepage','tagline','keywords','overview','production_companies','release_date','budget_adj','revenue_adj'], axis=1, inplace=True)

#check it out!
omv_df.info()


# In[9]:


# remove dublicate!
omv_df.drop_duplicates(inplace=True)


# In[10]:


# Drop null!
omv_df.dropna(inplace=True)


# In[11]:


omv_df.info()


# In[12]:


#check it!
omv_df.describe()


# In[13]:


#replacing 0 in 'revenue' , 'budget' and 'runtime' with the mean of each.

revenue_mean = omv_df['revenue'].mean()

omv_df['revenue'].replace(0, revenue_mean, inplace=True)

budget_mean = omv_df['budget'].mean()

omv_df['budget'].replace(0, budget_mean , inplace=True)

runtime_mean = omv_df['runtime'].mean()

omv_df['runtime'].replace(0, runtime_mean , inplace=True)



# In[14]:


omv_df.head(5)


# In[15]:


omv_df.info()


# In[16]:


omv_df.describe()


# Now the data looks clean, I can move to the next step and start exploring the data and answering the qustion posted early...

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.
# 
# 

# In[17]:


#visualize the data with histogram to have clera overlook
omv_df.hist(figsize=(13,8))


# ### Research Question 1 (What kinds of properties are associated with movies that have high revenues?)

# In[18]:


#Test the relationship between revenue and budjet and how the correlate with each other
omv_df.plot(x= 'budget', y='revenue', kind='scatter', title= "correlation budget and revenue", figsize=(12,8))


#  We can motice there is postive reltaionship betwen revenue and budget but it is not strong relationship 

# In[19]:


#Test the relationship between revenue and popularity and how the corllete with each other
omv_df.plot(x= 'popularity', y='revenue', kind='scatter', title= "correlation popularity and revenue", figsize=(12,8))


# Strong relationship betwen revenue and popularity!

# In[20]:


#Test the relationship between revenue and runtime and how the corllete with each other

omv_df.plot(x= 'runtime', y='revenue', kind='scatter', title= "correlation runtime and revenue", figsize=(12,8))


# Long run-time or short run-time dont have hight revenuew

# In[21]:


#Test the relationship between revenue and vote average and how the corllete with each other

omv_df.plot(x= 'vote_average', y='revenue', kind='scatter', title= "correlation vote_average and revenue", figsize=(14,8))


# Low votes film  from 1to 4 didnt get high revenuew  as from 5-8

# In[22]:


#Test the relationship between revenue and vote average and how the corllete with each other

omv_df.plot(x= 'release_year', y='revenue', kind='scatter', title= "correlation release_year and revenue", figsize=(14,8))


# We can notice that years have a strong relationship with revenue. the early tears starting from 1960 has less revenue than the latest.

# ### Research Question 2  - which year has the most number of film produced?
# 

# In[23]:


# Continue to explore the data to address your additional research
# the release years and the number of movies for each.
omv_df.release_year.value_counts().plot(kind='bar', figsize=(12,8));
plt.xlabel('yrars')
plt.ylabel('Number of Movies')
plt.title('Number of movies each year')


# In[24]:


#To check the exact number of each year

plt.xlabel('relese year')
plt.ylabel('Number of Movies')
plt.title('most film in year')
plt.hist(omv_df['release_year'], bins = 100)


#  Answering question 2. The year 2014 is the most year of produced films with 682 movies!

# ### Research Question 2  - which year has the most number of film produced?
# 

# In[25]:


#extract profit by sub bidget from revenue
#add a new column  name 'Movies Profit'
omv_df['Movies Profit'] = omv_df['revenue'] - omv_df['budget']


# In[26]:


#defining the function
def calculate(column):
    #for max revenues
    maxium_value  = omv_df[column].idxmax()
    omvdf_maxium  = pd.DataFrame(omv_df.loc[maxium_value])
    
    #for min revenues
    minium_value  = omv_df[column].idxmin()
    omvdf_minium  = pd.DataFrame(omv_df.loc[minium_value])
    
    #conact both df
    omvdf_maxium_minium = pd.concat([omvdf_maxium, omvdf_minium], axis=1)
    return omvdf_maxium_minium


# In[27]:


#call the function use below command

omvdf_x = calculate('Movies Profit')
columns = {omvdf_x.columns[0]:'MAx',omvdf_x.columns[1]:'Min'}
omvdf_x = omvdf_x.rename(columns = columns)
omvdf_x


# by using thr function above i was able to to get the ptofits of the movies and extract the highst film and the lowest in term of profits. 
# 
# The highst: Avatar
# The Lowest: The Warrior's Way
# 
# 
# #source :Github
# 

# <a id='conclusions'></a>
# ## Conclusions
# 
# 
# 
# To conclude, a data set from tmdb with more than 10k films has been investigated. 
# 
# Three questions have been answered. The first is what properties are associated with revenue? And we discovered by analysing the data that budget has strong relationships with revenue. also release years, where in the early years revenue were not much as the latest. 
#  The second question we answered which year has the most movies produced and after analysing we found that 2014 is the most yere films have been created with 680 films! The Third question is to identifet the highst and lowes profit film from the data swt. Avater is the higsy proftiable film wherase The Warrior's Way.  
#  
#  ## Limitation
#  
# The data set has issues such as missing data in columns, Null data, and duplicate data in the set, revenue and budget have 0 value in their rows. Some columns have been removed in the cleaning process and null data replaced with the mean of it. 

# In[28]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

