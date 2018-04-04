#!/usr/bin/env/ python
#encoding = "utf-8"

import nltk
from nltk.tokenize import word_tokenize

file = open('./article-essor.txt', 'rt')
article = file.read()

print(word_tokenize(article, language='french'))

file.close()
#destination.close()
