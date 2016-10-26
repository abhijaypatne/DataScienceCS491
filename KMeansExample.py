
# coding: utf-8

# In[1]:

from __future__ import print_function

from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn import metrics

from sklearn.cluster import KMeans, MiniBatchKMeans

import logging
from optparse import OptionParser
import sys
from time import time

import numpy as np


# In[3]:

categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
# Uncomment the following to do the analysis on all the categories
#categories = None

print("Loading 20 newsgroups dataset for categories:")
print(categories)


# In[6]:

dataset = fetch_20newsgroups(subset='all', categories=categories,
                             shuffle=True, random_state=42)


# In[ ]:




# In[7]:

print("%d documents" % len(dataset.data))
print("%d categories" % len(dataset.target_names))
print()


# In[8]:

print (type(dataset.data))


# In[10]:

#dataset.data[0]


# In[12]:

labels = dataset.target
true_k = np.unique(labels).shape[0]


# In[17]:

type(true_k)


# In[16]:

len(labels)


# In[18]:

true_k


# In[22]:

vectorizer = TfidfVectorizer(max_df=0.6, min_df=0.05, stop_words='english')


# In[25]:

x = vectorizer.fit_transform(dataset.data)


# In[27]:

type(x)


# In[28]:

x


# In[32]:

x[0][0]


# In[33]:

x.shape


# In[36]:

km = KMeans(n_clusters=5, init='k-means++', max_iter=100)


# In[37]:

km.fit(x)


# In[38]:

print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
print("Adjusted Rand-Index: %.3f"
      % metrics.adjusted_rand_score(labels, km.labels_))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(x, km.labels_, sample_size=1000))


# In[39]:

print("Top terms per cluster:")


# In[40]:

order_centroids = km.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()
for i in range(5):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()


# In[ ]:



