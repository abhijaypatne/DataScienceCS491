## Naive Bayes classifier for Tweet classification

# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import unicodedata as ud
from sklearn.metrics import precision_recall_fscore_support as prfs
import csv
import HTMLParser
from sklearn.metrics import classification_report
from sklearn.cross_validation import cross_val_score
from numpy import random
from nltk.stem.porter import PorterStemmer as porterStemmer
from itertools import izip
import collections
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_curve, auc


# In[2]:

def cleanTweet(originalTweet):
    htmlParser = HTMLParser.HTMLParser()

    tweet = originalTweet
    #tweet = htmlParser.unescape(originalTweet);
    #tweet = tweet.decode('windows-1252').encode('ascii', 'ignore')
    #tweet = tweet.decode('windows-1252')
    #tweet = tweet.decode("utf8").encode('ascii', 'ignore')
    #tweet = re.sub(r'[^\x00-\xFF]+', r'', tweet)
    #tweet = re.sub(r'[^\x00-\x7F]+', r'', tweet)
    #tweet = tweet.decode('utf-8').strip()
    #tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
    #tweet = tweet.encode('ascii','ignore')
    tweet = ''.join([i if ord(i) < 128 else ' ' for i in tweet])
    
    # remove URLs in tweet
    tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)

    # remove strings starting with @ in tweet
    tweet = re.sub(r'(\s)@\w+', r'', tweet)
    tweet = re.sub(r'@\w+', r'', tweet)
    
    # remove HTML tags from tweet
    tweet = re.sub('<[^<]+?>', '', tweet)

    # separates words joined with capital words.
    # E.g. DisplayIsAweson to Display Is Awesom
    #tweet = " ".join(re.findall('[A-Z][^A-Z]*', tweet));

    # remove exclamations
    tweet = re.sub(r'[<>!#@$:.,%\?-]+', r'', tweet)

    # remove extra white spaces
    tweet = re.sub(r'\s+', r' ', tweet)
    
    # stemming
    stemmer = porterStemmer()
    stemmedTweet = [stemmer.stem(word) for word in tweet.split(" ")]
    stemmedTweet = " ".join(stemmedTweet)
    
    tweet = str(stemmedTweet)
    tweet = tweet.replace("'", "")
    
    return tweet


# In[3]:

trainData = pd.read_csv("A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\hw4\\data\\train2Columns.csv")


# In[4]:

testData = pd.read_csv("A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\hw4\\data\\test2Columns.csv")


# In[5]:

trainData.shape
#data.head(2)


# In[6]:

rawTweetsSeries = trainData['tweets'];
tweetLabels = trainData['class'];


# In[7]:

rawTestTweetsSeries = testData['tweets'];
testTweetLabels = testData['class'];


# In[8]:

rawTestTweetsList = rawTestTweetsSeries.tolist()
testTweetLabelList = testTweetLabels.tolist()


# In[9]:

rawTweetsList = rawTweetsSeries.tolist()
tweetLabelList = tweetLabels.tolist()


# In[10]:

print (len(rawTweetsList))
print (rawTweetsList[0])
print (len(rawTestTweetsList))
print (rawTestTweetsList[0])


# In[11]:

randomTweets = random.choice(rawTweetsList, 3)
print (randomTweets)
randomTestTweets = random.choice(rawTestTweetsList, 3)
print (randomTestTweets)


# In[12]:

i = 0;
cleanedTweetsList = []
for tweet in rawTweetsList:
    #tweet.encode('utf-8').strip()
    #tweet = tweet.decode("utf8").encode('ascii', 'ignore')
    #print (i ,),
    cleanedTweet = cleanTweet(tweet).encode('ascii', 'ignore').strip();
    cleanedTweetsList.append(cleanedTweet);
    i += 1


# In[13]:

j = 0;
cleanedTestTweetsList = []
for tweet in rawTestTweetsList:
    cleanedTestTweet = cleanTweet(tweet).encode('ascii', 'ignore').strip();
    cleanedTestTweetsList.append(cleanedTestTweet);
    j += 1


# In[14]:

randomTweets = random.choice(cleanedTweetsList, 3)
print (randomTweets)
randomTestTweets = random.choice(cleanedTestTweetsList, 3)
print (randomTestTweets)


# In[15]:

# Create feature vectors
vectorizer = TfidfVectorizer(min_df=0.000125,
                             max_df = 0.75,
                             sublinear_tf=True,
                             use_idf=True)


# In[16]:

nbClassifier = BernoulliNB()


# In[17]:

trainVectors = vectorizer.fit_transform(cleanedTweetsList)
trainVectors.shape


# In[18]:

testVectors = vectorizer.transform(cleanedTestTweetsList)
testVectors.shape


# In[19]:

nbClassifier.fit(trainVectors, tweetLabelList)


# In[20]:

predictedLabels = nbClassifier.predict(testVectors)


# In[21]:

predictedLabelList = predictedLabels.tolist()


# In[22]:

classActual = np.array(testTweetLabels)
classPredicted = np.array(predictedLabelList)


# In[23]:

#prfs(classActual, classPredicted)


# In[24]:

target_names = ['0', '1']


# In[25]:

print(classification_report(testTweetLabels, predictedLabelList, target_names=target_names))


# In[26]:

print("Confusion matrix")
print (confusion_matrix(testTweetLabels, predictedLabels))


# In[27]:

counter=collections.Counter(testTweetLabels)
print("Actual values: "),
print (counter)


# In[28]:

counter=collections.Counter(predictedLabels)
print("Actual values: "),
print(counter)


# In[29]:

testAccuracy = nbClassifier.score(testVectors, testTweetLabels)
print ("Test accuracy:"),
print (testAccuracy)


# In[30]:

trainAccuracy = nbClassifier.score(trainVectors, tweetLabels)
print ("Train accuracy:"),
print (trainAccuracy)


# In[31]:

cvScores = cross_val_score(nbClassifier, trainVectors, tweetLabelList, cv=10)
print ("Cross validation scores:"),
print (cvScores)
print ("Mean: ", cvScores.mean())
print ("Minimum: ", cvScores.min())
print ("Maximum: ", cvScores.max())


# In[32]:

xAxis = [x for x in range(1,13)]
yAxis = cvScores.tolist()
yAxis.extend([trainAccuracy, testAccuracy])


# In[33]:

plt.plot(xAxis, yAxis, marker='o', linestyle='--', color='r')
plt.xlabel("Cross validation round number")
plt.ylabel("Accuracy")
plt.title("Naive Bayes Accuracy for 10 fold Cross Validation")
plt.text(7, .795, "11=train, 12=test")
plt.show()


# In[34]:

# Question 10


# In[35]:

predictionProbabilities = nbClassifier.predict_proba(testVectors)
zeroProbs = predictionProbabilities[:, 1]
oneProbs = predictionProbabilities[:, 0]
topFiveOne = oneProbs.argsort()[-5:][::-1]


# In[36]:

print ("Correctly classified probabilities:")
print ("------------------------------------------------------------------------------")
print ("tweetid \t tweet \t actual label \t predited label \t prediction probability");
print ("------------------------------------------------------------------------------")
for x in topFiveOne:
    print (x),
    print (rawTestTweetsList[x]),
    print (testTweetLabelList[x]),
    print (predictedLabelList[x])
    print (predictionProbabilities[x][0])


# In[37]:

# Question 7


# In[38]:

featureNames = vectorizer.get_feature_names()
coefficientArray = nbClassifier.coef_[0]
top20Features = coefficientArray.argsort()[-20:][::-1]


# In[39]:

print ("Top 20 features:")
for x in top20Features:
    print (featureNames[x]),


# In[40]:

# Question 7


# In[41]:

#fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
fpr, tpr, thresholds = metrics.roc_curve(testTweetLabelList, predictedLabelList)
roc_auc = auc(fpr, tpr)


# In[42]:

plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Naive Bayes")
plt.show()

