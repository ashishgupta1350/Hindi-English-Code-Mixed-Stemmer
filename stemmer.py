#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import os
try:
    import nltk
except:
    print("First install NLTK using pip install nltk command")
    exit()
try:
    import gensim
    from gensim import corpora, models, similarities
except:
    print("First install Gensim using pip install nltk command")
    exit()

    
class Stemmer:
    w2vModel = None
    sensitivity = 10
    
    # constructor
    def __init__(self, modelLocation= "w2vModel", w2vModel = None):
        try:
            self.w2vModel = gensim.models.Word2Vec.load(modelLocation)
        except:
            print("Could not locate the w2vModel file in the directory : "+(modelLocation))
            print("Try to load the w2vModel and try again")
    
        
    
    #  ----------- Stemming functions -----------
    
    
    # takes a word and removes the repeated occurance of characters in that word
    # outputs word without repeat consecutive occurance of the word
    def RepetitionStemmer(self, word):
        # find repeted occurence of letters in a word
        # remove the occurence 
        i=0
        newWord = ''
        while(i <len(word)):
            c = word[i]
            newWord+=c
            while(i<len(word) and word[i] == c):
                i=i+1

        return newWord

    # takes a word2vec model, word and nWords(to run most similar on - higher the better but slower)
    # output the list of words similar to that word ( including that word passed through repetition stemmer)
    def WordEmbeddingStemmer(self, w2vModel, word, nWords = 10):

        try:
            similarWordsList =[w2vModel.wv.most_similar(word, topn = nWords )[i][0] for i in range(10)]
        except:
            return self.RepetitionStemmer(word)

        word = self.RepetitionStemmer(word)

        outputList = []
        for similarWord in similarWordsList:
            stemmSimilarWord = self.RepetitionStemmer(similarWord)
            w0 = word
            w1 = word[:-1]
            sw0 = stemmSimilarWord
            sw1 = stemmSimilarWord[:-1]

            if (sw0 in w0) or( w0 in sw0) or (sw1 in w0) or (w1 in sw0):
                if(len(stemmSimilarWord)<len(word)):
                    outputList.append(stemmSimilarWord)
                else:
                    outputList.append(word)
        if len(outputList) == 0:
            outputList.append(word)
        return outputList[0]
    
    # stemmers
    def stemWord(self, word):
        return self.WordEmbeddingStemmer(self.w2vModel, word)
    
    def stemListOfWords(self, listOfWords):
        return [self.WordEmbeddingStemmer(self.w2vModel, word) for word in listOfWords]
    
    def stem2dListOfWords(self, listOfWords2d):
        output = []
        for sentenceOfWords in listOfWords2d:
            output.append([self.WordEmbeddingStemmer(self.w2vModel, word) for word in sentenceOfWords])
        return output
    

