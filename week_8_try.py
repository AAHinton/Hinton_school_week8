#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import geopandas as gpd


# In[3]:


import matplotlib.pyplot as plt


# In[16]:


import numpy as np


# In[5]:


import fiona


# In[6]:


import arcpy


# In[7]:


from arcgis.gis import GIS


# In[8]:


import shapely


# In[11]:


drinks=pd.read_csv('C://Users/hinto/Desktop/School/Python_course/data/drinks.csv')


# In[12]:


drinks.head()


# In[18]:


#maybe try to make things up to do bar graph instead of using real data first

#stacked bar plot


# In[17]:


nationality = ("American", "German", "Italian")
summer_drinks={
    "wine": np.array([3,1,5]),
    "beer": np.array([4,7,1]),
    }
width=0.5
fig, ax=plt.subplots()
bottom=np.zeros(3)
for boolean, summer_drinks in summer_drinks.items():
    p=ax.bar(nationality, summer_drinks, width, label=boolean, bottom=bottom)
    bottom+=summer_drinks
    
ax.set_title("Number of drinks on weekends during summertime")
ax.legend(loc="upper right")

plt.show()


# In[20]:


#try number 2 for made up matplotlib plot
#scatter plot with histograms example first then try to make my own


# In[21]:


import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# some random data
x = np.random.randn(1000)
y = np.random.randn(1000)


def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')


# In[22]:


# Start with a square Figure.
fig = plt.figure(figsize=(6, 6))
# Add a gridspec with two rows and two columns and a ratio of 1 to 4 between
# the size of the marginal Axes and the main Axes in both directions.
# Also adjust the subplot parameters for a square plot.
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# Create the Axes.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)


# In[27]:


#could not follow what changes would do so will try another type
#stackplot attempt


# In[28]:


import matplotlib.ticker as mticker


# In[29]:


#make up data for weekly alcohol drinks by age


# In[35]:


age=[15, 20, 21, 25, 30, 50]
drinks_pp={
    'Americans': [1, 3, 6, 5, 7, 2],
    'Germans': [1,4,6,6,4,4],
    'Italians': [1,3,3,4,4,5],
}

fig, ax=plt.subplots()
ax.stackplot(age, drinks_pp.values(), 
            labels=drinks_pp.keys(), alpha=0.8)
ax.legend(loc='upper left')
ax.set_title('Weekly Drinks per person at Age')
ax.set_xlabel('Age')
ax.set_ylabel('Weekly Drinks')
ax.yaxis.set_minor_locator(mticker.MultipleLocator(.5))
plt.show()


# In[ ]:




