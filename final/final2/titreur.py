#!/usr/bin/env/ python
#encoding = "utf-8"

#Librairies
import nltk
import random

#import nltk.data

from nltk.tokenize import word_tokenize
from nltk import pos_tag

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

#Run
article = tokenize_text(source0)
out = clean_text(article)

#Définition adjectif
file1 = open('./dico/adjectif.txt', 'rt')
adjectif = file1.read()
adjectif2 = adjectif.split()
listAdjectif = " ".join(set(out) & set(adjectif2))
listAdjectif2 = listAdjectif.split()

'''
#Définition adverbe
file2 = open('./dico/adverbe.txt', 'rt')
adverbe = file1.read()
adverbe2 = adverbe.split()
listAdverbe = set(out) & set(adverbe2)
'''

#Définition article
file3 = open('./dico/article.txt', 'rt')
article = file3.read()
article2 = article.split()
listArticle = " ".join(set(out) & set(article2))
listArticle2 = listArticle.split()

#Définition conjonction
file4 = open('./dico/conjonction.txt', 'rt')
conjonction = file4.read()
conjonction2 = conjonction.split()
listConjonction = " ".join(set(out) & set(conjonction2))
listConjonction2 = listConjonction.split()

'''
#Définition liaison
file5 = open('./dico/liaison.txt', 'rt')
liaison = file5.read()
liaison2 = liaison.split()
listLiaison = set(out) & set(liaison2)
'''

#Définition nom
file6 = open('./dico/nom.txt', 'rt')
nom = file6.read()
nom2 = nom.split()
listNom = " ".join(set(out) & set(nom2))
listNom2 = listNom.split()

'''
#Définition onomatopé
file6 = open('./dico/onomatope.txt', 'rt')
onomatope = file6.read()
onomatope2 = onomatope.split()
listOnomatope = set(out) & set(onomatope2)
'''

#Définition préposition
file7 = open('./dico/preposition.txt', 'rt')
preposition = file7.read()
preposition2 = preposition.split()
listPreposition = " ".join(set(out) & set(preposition2))
listPreposition2 = listPreposition.split()

#Définition pronom ???
file8 = open('./dico/pronom.txt', 'rt')
pronom = file8.read()
pronom2 = pronom.split()
listPronom = " ".join(set(out) & set(pronom2))
listPronom2 = listPronom.split()

#Définition verbe
file9 = open('./dico/verbe.txt', 'rt')
verbe = file9.read()
verbe2 = verbe.split()
listVerbe = " ".join(set(out) & set(verbe2))
listVerbe2 = listVerbe.split()
#print(listVerbe)

#print(listVerbe)
print(random.choice(listArticle2)+' '+random.choice(listNom2)+ ' ' +random.choice(listVerbe2)+ ' '+ random.choice(listAdjectif2)+ ' ' +random.choice(listNom2))

file0.close()
file1.close()
#file2.close()
file3.close()
file4.close()
#file5.close()
#file6.close()
file7.close()
file8.close()
file9.close()
