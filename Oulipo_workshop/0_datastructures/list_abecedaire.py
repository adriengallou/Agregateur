#!/usr/bin/python
#encoding = utf-8
# this is a shebang: https://en.wikipedia.org/wiki/Shebang_%28Unix%29

'''
This script takes a sentence you write in the terminal, and gives it back in alphabetical order
A list is ordered and changeable. It is less efficient than a set/tuple. But it allows to work with index numbers.
Check out other options for list comprehension: https://docs.python.org/3/tutorial/datastructures.html
Made for OLA #5, Paris, 15-17 décembre 2017
'''

# Déclaration variable chaine de caractère
sentence = "Les gouvernements suspectent la littérature parce qu’elle est une force qui leur échappe"

# Affichage
print("phrase originale:", sentence)

# Découpe
words = sentence.split()
print(words)

# sort words of list
words.sort()

# print sorted wordlist as string
print("phrase alphabétique:", " ".join(words).capitalize(), '.')
