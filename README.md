# Hindi-English-Code-Mixed-Stemmer
An unsupervised stemmer for Natural Language Processing Tasks on Hinglish Language ( Hindi + English words )
### Requirements
* Gensim
* NLTK

Usage:

```
import stemmer
```

#### Single Word Stemmer

```
myStemmer = stemmer.Stemmer()
output = myStemmer.stemWord("ladkaa")
```
> output : 'ladka'

#### List of Words Stemmer
```
output = myStemmer.stemListOfWords(["ladkii", "ladkaaaa", "firaaangii"])
```
> output: ['ladki', 'ladka', 'firangi']

#### 2D List of Words Stemmer
```    
output = myStemmer.stem2dListOfWords([["merii","merraa"], ["terii", "terraaa", "aaajjjaa"]])
```
> output: [['meri', 'mera'], ['teri', 'tera', 'aja']]


##### Use Credits:
Ashish Gupta
Github: www.github.com/ashishgupta1350
You are free to use and distribute this in anyway you like.
