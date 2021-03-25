#!/usr/bin/env python
# coding: utf-8

# In[49]:



# By Alberto Diaz Durana
# adiazdurana@gmail.com
# 25.03.2021

# Assignment:  https://gist.github.com/maxjakob/f6670bfbe7f3c38efb8df46efdf4ca27


# In[50]:


import pandas as pd
import numpy as np
import requests

r = requests.get('https://raw.githubusercontent.com/localytics/data-viz-challenge/master/data.json')

j = r.json()


# In[51]:


#j


# This is a Nested JSON structure. This means that each key can have more keys associated with it. So we need to parse it!

# In[52]:


nested_json = j


# Next, we will flatten the JSON using the normalize function. We will pass in the complete data for now and see how it looks.

# In[53]:


from pandas import json_normalize
df = json_normalize(nested_json['data'])


# In[54]:


#df.head()


# In[55]:


#Only entries of female ("gender": "F") and Californian ("state": "CA") users should be considered.

df = df[(df['gender']=='F') & (df['location.state']=='CA')].reset_index(drop=True)


# In[56]:


# date has the format of YYYY-MM-DD and is based on client_time.

df['date'] = pd.to_datetime(df.client_time, unit='s', errors='coerce')
#df['date'].head()


# In[57]:


df['date'] = pd.to_datetime(df['date']).dt.date
#df['date'].head()


# In[58]:


# count is the count of entries.

df['count'] = np.arange(1, len(df)+1)


# In[68]:


#df.head()


# In[60]:


# amount_sum is the sum the values in the amount field.

df['amount_sum'] = df['amount'].sum()


# In[61]:


# Output the following columns: age, device, date, count, amount_sum.

total_events = df.filter(['age', 'device', 'date', 'count', 'amount_sum'], axis=1)


# In[62]:


#total_events.head()


# Now we write the the DataFrame directly into the S3 bucket in AWS

# In[63]:


#total_events.to_csv('total_events.csv', sep='\t')

# Copy s3 URI from the bucket
bucket_name = 's3://add-total-events/tmp_csv'
file_name ='total_events.csv'


# In[64]:


# Place the file my_secrets in your lib located in the path for your env .conda\envs\envADD\lib
# If you want to enter the aws dashboard the login credentials are located in this same file

from my_secrets import access_key, secret_access_key

import boto3
from io import StringIO

bucket_name = 'add-total-events'

df = total_events

csv_buffer = StringIO()
df.to_csv(csv_buffer)

client = boto3.client('s3',
                      aws_access_key_id = access_key,
                      aws_secret_access_key = secret_access_key)

response = client.put_object(
    ACL = 'private',
    Body = csv_buffer.getvalue(),
    Bucket = bucket_name,
    Key = file_name
    )


# In[65]:


#response


# In[66]:


# to verify we will import the file back to a dataframe
from io import BytesIO

bucket, filename = bucket_name, file_name

s3 = boto3.resource('s3',
                      aws_access_key_id = access_key,
                      aws_secret_access_key = secret_access_key)

obj = s3.Object(bucket, filename)
with BytesIO(obj.get()['Body'].read()) as bio:
    df_check = pd.read_csv(bio)


# In[67]:


print('The file has been succesfuly pushed to the aws s3 bucket')
print('________________________________________________________________________________')
print(df_check)

