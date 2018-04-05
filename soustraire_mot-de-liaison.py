#!/usr/bin/env/ python
#encoding = "utf-8"

import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

nmin = input("Nombre minimal de caractères pour mot sélectionné:")

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
        if len(word) > int(nmin):
        	# remove capital letters (string operation)
        	word = word.lower()
        	# Clean punctuation (string operation)
        	word = word.strip(" ;''?:,()!.\").”-«»’1234567890")
        	# add word to new word list
        	new_word.append(word)

    return new_word

#Supprime stopper français
def clean_stop(text):

    for word in text:
        if word in stopwords.words('french'):
            text.remove(word)

    text2 = pos_tag(text, lang='fr')
    #print(text2)

    '''
    for element in text2:
        if element[1] == 'NN':
            print("ca marche")
    '''
    
    return text2


'''
with open('./dico.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[4])
'''

#Run
article = tokenize_text(source0)
out = clean_text(article)
out2 = clean_stop(out)
#Affiche le résultat
print(out2)

file0.close()
