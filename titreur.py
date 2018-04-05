#!/usr/bin/env/ python
#encoding = "utf-8"

import nltk

#import nltk.data

from nltk.tokenize import word_tokenize
from nltk import pos_tag


#frenchtag = nltk.data.load('/taggers/universal_tagset/fr-paris.map')


#Ouvre les sources
file0 = open('./article-essor.txt', 'rt')
source0 = file0.read()

#Coupe la source en mot et le stocke dans un tableau => article
def tokenize_text(text):

    return word_tokenize(text, language='french')

#Trie dans le tableau article, supprime la ponctuation, supprime les mots inférieur à nmin
def clean_text(text):

    new_word = []

    for word in text:
        # remove capital letters (string operation)
        word = word.lower()
        # Clean punctuation (string operation)
        word = word.strip(" ;''?:,()!.\").”-«»’1234567890")
        # add word to new word list
        if word:
            new_word.append(word)

    return new_word

#Indique le genre du mot
def clean_stop(text):

    text = pos_tag(text, lang='fr')

    return text

def extract(texte, tag):
    liste = []
    for word, pos in out2:
        if pos == tag:
            liste.append("'" + word + "' "+tag)
    return liste



#Run
article = tokenize_text(source0)
out = clean_text(article)
out2 = clean_stop(out)
out3 = extract(out2, "NN")
#Affiche le résultat
print(out3)

file0.close()
