
# coding: utf-8

# In[2]:

import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


# In[31]:

correction("Ecology")


# In[11]:

def jaccard(a,b):
    a=a.split()
    b=b.split()
    union = list(set(a+b))
    intersection = list(set(a) - (set(a)-set(b)))
    print "Union - %s" % union
    print "Intersection - %s" % intersection
    jaccard_coeff = float(len(intersection))/len(union)
    print "Jaccard Coefficient is = %f " % jaccard_coeff


# In[13]:

jaccard('models and algorithms', 'modelz and algorithmz')


# In[14]:

import difflib


# In[15]:

a = "models and algorithms"
b = "modelz and algorithmz"
seq=difflib.SequenceMatcher(a=a.lower(), b=b.lower())
seq.ratio()


# In[16]:

str = "parallel computation: models, algorithms, limits|Filtering and Prediction of Hidden Markov Models"
strlist = str.split("|")


# In[18]:

strlist[0].split()


# In[19]:

import re


# In[28]:

re.split('(\W)', 'photo-lab')


# In[ ]:



