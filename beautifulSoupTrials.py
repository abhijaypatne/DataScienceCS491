
# coding: utf-8

# In[2]:

from bs4 import BeautifulSoup
import urllib2
import csv


# In[3]:

from urllib import urlopen


# In[4]:

data = open("A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\DataScienceCS491\\superbowl.html", "r").read()


# In[5]:

#diagnose(data)


# In[6]:

soup = BeautifulSoup(data, "html.parser")


# In[7]:

mysoup=BeautifulSoup(urlopen('https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions').read(),'html.parser')


# In[8]:

type(mysoup)


# In[9]:

soupData.head(2)


# In[10]:

results = mysoup.find_all("table", { "class" : "wikitable sortable" })


# In[14]:

tables = mysoup.find_all("table", { "class" : "wikitable sortable" });
reqTable = tables[1];
for row in reqTable.findAll("tr")[1:]:
    columns = row.findAll("td");
    number = columns[0].find('a').get_text().strip();
    print (number),


# In[15]:

type(results)


# In[16]:

#print results


# In[17]:

table = results[1]


# In[18]:

type(table)


# In[72]:

str = (table.findAll("tr")[24].findAll("td")[0].find('a').get_text()).strip()


# In[76]:

str.encode('ascii', 'ignore')


# In[20]:

type((table.findAll("tr"))[20].findAll("td"))


# In[21]:

str = (table.findAll("tr")[24].findAll("td")[0].find('a'))


# In[61]:

print table.findAll("tr")[24].findAll("td")[1].findAll("span")[-1].get_text()[-4:]


# In[42]:

print table.findAll("tr")[1].findAll("td")[2].find('a').get_text()


# In[55]:

print table.findAll("tr")[1].findAll("td")[3].findAll("span")[-1].get_text()


# In[87]:

print table.findAll("tr")[51].findAll("td")[4].find('a').get_text()


# In[90]:

print table.findAll("tr")[51].findAll("td")[4].findAll("span")[-1].get_text()


# In[64]:

print table.findAll("tr")[1].findAll("td")[5].find('a').get_text()


# In[85]:

print table.findAll("tr")[1].findAll("td")[5].findAll("span")[-1].get_text()


# In[ ]:



