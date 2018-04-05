#!/usr/bin/env/ python
#encoding = "utf-8"

import nltk
from nltk.tokenize import word_tokenize

#Ouvre les sources
file0 = open('./article-essor.txt', 'rt')
source = file0.read()

file1 = open('./dico.txt', 'rt')
dico = file1.read()

#Coupe la source en mot et le stocke dans un tableau => article
def tokenize_text(text):
    return word_tokenize(text, language='french')

#Trie dans le tableau article, supprime la ponctuation, supprime les mots inférieur à trois lettres
def clean_text(text):

    new_word = []

    for word in text:
        if len(word) > 3:
        	# remove capital letters (string operation)
        	word = word.lower()
        	# Clean punctuation (string operation)
        	word = word.strip(" ;''?:,()!.\").”-«»’1234567890")
        	# add word to new word list
        	new_word.append(word)

    return new_word

#Run
article = tokenize_text(source)
out = clean_text(article)

#Affiche le résultat
print(out)


file0.close()
file1.close()
