
# coding: utf-8

# In[2]:

#script to read files (each file is a document content in raw json format) from a 
#specified folder and write to a MongoDB collection
#Have mongod.exe and mongo.exe running (in that order) when you execute this code

##Databases contains collections. A collection is made up of documents.
##Each document is made up of fields!


# In[5]:

#using pymongo and json
import pymongo
import json


# In[6]:

#Connection to Mongo DB
try:
    conn=pymongo.Connection()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
conn


# In[7]:

#Set basepath
basepath = 'D:\Side Projects\Python\Aaron\GET\Aaron_subfolder_copy\data'


# In[8]:

#Read filenames into file_names
file_names = []
#Set value for range; 1 for now - just read the first file
for j in range(4):
    for i in range(99):
        file_names.append(basepath+'\microsoft-excel_'+str(j)+'_'+str(i))


# In[9]:

#Define my mongoDB database
db = conn.odesk_files


# In[16]:

#Define my collection where I'll insert my search
#Get a collection
collection = db.my_collection


# In[11]:

#Display database names created
conn.database_names()


# In[12]:

#Display collection names created
db.collection_names()


# In[17]:

#Remove database odesk_files
#conn.drop_database("odesk_files")
#check!
#conn.database_names()


# In[15]:

#Delete a collection
#conn.odesk_files.drop_collection("my_collection")
#check!
#conn.odesk_files.collection_names()


# In[17]:

#process each file sequentially
for i in range(len(file_names)):
    with open(file_names[i],'r') as record:
        data=record.read()
    ##print data to see what is read
    #print data
    #insert document into collection
    doc=json.loads(data)
    doc["rate"]=float(doc["rate"])
    collection.insert(doc)


# In[18]:

#Display number of documents in the collection
collection.count()


# In[19]:

##Queries
#1. Number of Macedonian profiles
collection.find({"country": "Macedonia"}).count()


# In[20]:

#2. Names of those Macedonian members
search_docs = collection.find({"country": "Macedonia"})
for this_document in search_docs:
    print this_document["name"]


# In[21]:

#3. Number of Indian profiles specifying MS Excel as a skill
collection.find({"country": "India","skills": "microsoft-excel"}).count()


# In[22]:

#4. Using Regex to find a profiles which are hard-working
import re
regex = re.compile(r'hardworking|hard work|hard working')
rstats = collection.find({"description":regex}).count()
rstats
#print collection.find({"description":regex})


# In[28]:

#!5. Profiles created between specified dates
#from datetime import datetime
#date1 = datetime.strptime("June 17, 2010", "%B %e, %Y")
#date2 = datetime.strptime("August 20, 2011", "%B %e, %Y")
# Between 2 dates
#collection.find({"member_since": {"$gte": date1, "$lt": date2}}).count()


# In[23]:

#6. What skills and categories do profiles with maximum rates have?
skillset=[]
type_of_work=[]
rates=[]
max_rate = collection.find().sort([("rate", pymongo.DESCENDING)]).limit(20)
for this_document in max_rate:
    print('\n')
    print this_document["skills"]
    skillset=skillset+this_document["skills"]
    print this_document["categories"]
    type_of_work=type_of_work+this_document["categories"]
    print this_document["rate"]
    rates.append(this_document["rate"])
import collections
counter1 = collections.Counter(skillset)
counter2 = collections.Counter(type_of_work)
counter3 = collections.Counter(rates)
print counter1.most_common() #WHY DOESN'T THIS PRINT?
print counter2.most_common()
print counter3.most_common()


# In[24]:

#Skills that get paid well
val_vec=[]
key_vec=[]
for key,val in counter1.items():
    val_vec.append(val)
    key_vec.append(key) 
        
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

y_pos = np.arange(len(key_vec))

plt.barh(y_pos, val_vec, xerr=0, align='center', alpha=0.7)
plt.yticks(y_pos, key_vec)
plt.xlabel('Skill frequency among profiles')
plt.title('Skills that get paid well')

plt.show()


# In[25]:

#Categories that get paid well
val_vec=[]
key_vec=[]
for key,val in counter2.items():
    val_vec.append(val)
    key_vec.append(key) 
        
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

y_pos = np.arange(len(key_vec))

plt.barh(y_pos, val_vec, xerr=0, align='center', alpha=0.7)
plt.yticks(y_pos, key_vec)
plt.xlabel('Category frequency among profiles')
plt.title('Categories that get paid well')

plt.show()


# In[26]:

#Histogram of rates
val_vec=[]
key_vec=[]

list=counter3.items()
list.sort(key=lambda x: [x[0]])
for key,val in list:
    val_vec.append(val)
    key_vec.append(key) 

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

y_pos = np.arange(len(key_vec))

plt.barh(y_pos, val_vec, xerr=0, align='center', alpha=0.7)
plt.yticks(y_pos, key_vec)
plt.xlabel('Rate frequency among profiles')
plt.title('Rates that are high')

plt.show()


# In[27]:

#7. Demographics of the members (Top 30 countries by oDesk popularity)
countries=[]
country_list=collection.find()
for this_document in country_list:
    #print this_document["country"]
    countries.append(this_document["country"])
import collections
counter4 = collections.Counter(countries)
counter4.most_common(30)

val_vec=[]
key_vec=[]
for key,val in counter4.items():
    val_vec.append(val)
    key_vec.append(key) 
        
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

y_pos = np.arange(len(key_vec))

plt.barh(y_pos, val_vec, xerr=0, align='center', alpha=0.7)
plt.yticks(y_pos, key_vec)
plt.xlabel('Country frequency among profiles')
plt.title('Top 30 countries by oDesk popularity')

plt.show()

