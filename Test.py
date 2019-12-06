#!/usr/bin/env python
# coding: utf-8

# In[1]:


import stemmer


# In[8]:


myStemmer = stemmer.Stemmer()
output = myStemmer.stemWord("ladkaa")
if(output == "ladka"):
    print("Function stemWord passed! ")


# In[9]:


output = myStemmer.stemListOfWords(["ladkii", "ladkaaaa", "firaaangii"])
if(output[0]=='ladki' and output[1]=='ladka' and output[2]=='firangi'):
    print("Function stemListOfWords passed!")
    


# In[18]:


output = myStemmer.stem2dListOfWords([["merii","merraa"], ["terii", "terraaa", "aaajjjaa"]])
if(output[0][0]=='meri' and output[0][1]=='mera' and output[1][0]=='teri' and output[1][2]=='aja' ):
    print("Function stem2dListOfWords passed!")
    

