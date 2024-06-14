#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import geopandas as gpd


# In[3]:


import numpy as np


# In[4]:


import arcpy


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


df=pd.DataFrame()


# In[7]:


from geodatasets import get_path


# In[9]:


parcel=gpd.read_file('C:/Users/hinto/Desktop/School/GIS6345_Program/week_5_pandas/assignment_P2_shape/Final_10_parcels.shp')
parcel


# In[10]:


parcel.plot(figsize=(15,15))


# In[11]:


#not what the problem is asking.....plot a grpah of attribute
#i dont think this has a good attribute to plot area vs. what?
#need to get other data and maybe plot parcels per county or something if I can figure out how


# In[12]:


limited_parcels=gpd.read_file('C:/Users/hinto/Desktop/School/old classes/GIS5201/GIS_final_project/New choices/VA_parcels_v3.shp')
limited_parcels.head()


# In[13]:


#plot locatlity vs acres maybe?


# In[14]:


#would need to call location of data points for my x,y like 2 and 7 position minus header


# In[15]:


limited_parcels.plot();


# In[29]:


#chloropleth map of acres
limited_parcels.plot(column="Acres")


# In[22]:


from arcgis import GIS
gis=GIS()


# In[24]:


m1=GIS().map("Virginia")
m1


# In[28]:


item=gis.content.get("C:/Users/hinto/Desktop/School/old classes/GIS5201/GIS_final_project/New choices/VA_parcels_v3.shp")
flayer=item.layers[7]
df=flayer.query(where="Acres<25").sdf


# In[26]:


limited_parcels.tail()


# In[27]:


limited_parcels.spatial.plot(map_widget=m1)


# In[30]:


import geodatasets


# In[31]:


limited_parcels=gpd.read_file('C:/Users/hinto/Desktop/School/old classes/GIS5201/GIS_final_project/New choices/VA_parcels_v3.shp')
limited_parcels.head()


# In[32]:


parcels=limited_parcels.set_index("LOCALITY")


# In[33]:


parcels["area"]=parcels.area
parcels["area"]


# In[34]:


parcels["boundary"]=parcels.boundary
parcels["boundary"]


# In[35]:


parcels.plot("area", legend=True)


# In[36]:


parcels.explore("area", legend=False)


# In[39]:


limited_parcels.plot(kind="bar", x="LOCALITY", y="Acres")


# In[ ]:




