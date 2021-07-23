#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import requests.auth


# In[7]:


client_auth = requests.auth.HTTPBasicAuth('92FCO5BodoDM6Q','37dv3TSC4axJAJnvNaz2af48csW6Hw')
post_data = {"grant_type" : "password", "username": "Solid_Perspective_59", "password": "rania8991"}
headers = {'User-agent': 'Formation'}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth = client_auth, data = post_data, headers = headers)
response.json()


# In[9]:


headers = {"Authorization" : "bearer 980183604953-ieg_hbfuhY9hYEHOLQOV7tHTeuO0bQ", "User-agent": "Formation"}
params = {"t" : "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers , params=params)
python_top = response.json()
print(python_top)


# # Obtenir le post avec le plus de votes

# In[14]:


python_top_articles = python_top['data']['children']
most_upvoted = ""
most_upvotes = 0

for article in python_top_articles : 
    ar = article['data']
    if ar["ups"]>= most_upvotes :
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]
        
print (most_upvoted)
print (most_upvotes)


# In[20]:


response = requests.get("https://oauth.reddit.com/r/python/comments/oekhvs", headers = headers)
comments = response.json()
print(comments)


# In[21]:


comments[1]['data']['children']


# In[25]:


top_comment = comments[1]['data']['children']
most_upvoted = ""
most_upvotes = 0
for comment in top_comment :
    com = comment['data']
    if com["ups"]>= most_upvotes :
        most_upvoted = com["id"]
        most_upvotes = com["ups"]
print ( most_upvoted)       
print ( most_upvotes)


# In[ ]:




