#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
dataframe = pd.read_csv('FIFA23_official_data.csv')
dataframe.shape


# In[10]:


dataframe.describe()


# In[11]:


dataframe.values


# In[27]:


df1 = pd.DataFrame(dataframe, columns=['Name', 'Wage', 'Value'])
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0
wage = df1['Wage'].replace('[\€,]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€,]', '', regex=True).apply(value_to_float)

df1['Wage'] = wage
df1['Value']= value
df1['difference']= df1['Value']-df1['Wage']
df1.sort_values('difference', ascending=False)


# In[30]:


import seaborn as sns
sns.set()
graph = sns.scatterplot(x='Wage', y='Value', data=df1)
graph
