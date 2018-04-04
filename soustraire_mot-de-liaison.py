#!/usr/bin/env/ python
#encoding = "utf-8"

import nltk
from nltk.tokenize import word_tokenize

file = open('./article-essor.txt', 'rt')
article = file.read()

article = word_tokenize(article, language='french')

new_word = []

for word in article:
    if len(word) > 3:
    	# remove capital letters (string operation)
    	word = word.lower()
    	# Clean punctuation (string operation)
    	word = word.strip(" ;''?:,()!.\").”-«»’")
    	# add word to new word list
    	new_word.append(word)

print(new_word)


file.close()
#destination.close()
