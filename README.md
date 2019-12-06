# Hindi-English-Code-Mixed-Stemmer
An unsupervised stemmer for Natural Language Processing Tasks on Hinglish Language ( Hindi + English words )

<div align="center">

[![Build Status](https://img.shields.io/travis/dwyl/hits/master.svg?style=flat-square)](https://travis-ci.org/dwyl/hits)
[![ashishgupta1350](https://img.shields.io/codecov/c/github/dwyl/hits/master.svg?style=flat-square)](http://codecov.io/github/dwyl/hits?branch=master)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](https://github.com/dwyl/hits/issues/74)

<!-- Docs badge not working ... if you have time to help investigate, please do.
[![Inline docs](http://inch-ci.org/github/dwyl/hits.svg?style=flat-square)](http://inch-ci.org/github/dwyl/hits)
-->

</div>

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
