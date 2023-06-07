#!/usr/bin/env python
# coding: utf-8

# In[41]:


#First, let's import the dataset
from sklearn.datasets import load_iris
iris = load_iris()


# In[42]:


#let's split up our data into a training and a target portion in the next two cells
X=iris.data
y=iris.target
feature_names = iris.feature_names
target_names = iris.target_names
from sklearn.model_selection import train_test_split


# In[43]:


#let's select the amount of data on the training and testing sides
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape)
print(X_test.shape)


# In[44]:


#Now, we import our machine learning algorithm
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


# In[45]:


#we can import a metric to tell us how accurate we are
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))


# In[46]:


#Now let's imput a made-up sample to predict the sample species
sample= [[3, 5, 4, 2], [2, 3, 5, 4]]
predictions = knn.predict(sample)
pred_species = [iris.target_names[p] for p in predictions]
print('predictions:', pred_species)


# In[52]:


#let's save this model for future use
import joblib
joblib.dump(knn, 'irisml.joblib')
iris_model = joblib.load('irisml.joblib')


# In[ ]:




