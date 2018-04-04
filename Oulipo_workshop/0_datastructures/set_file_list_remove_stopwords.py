#!/usr/bin/env python
# -*- coding: utf-8 -*-


 #    Copyright (C) 2016 Constant, Algolit
 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details: <http://www.gnu.org/licenses/>.


'''
Input texts are checked against occurences of certain words included in a list of "stopwords" established by NLTK (Natural Language Toolkit). These words are then removed.
In data mining, text processing and machine learning, these so-called high frequency words are filtered out before or after natural language data is processed. 
Relational words such as 'the', 'is', 'at', 'which', and 'on' are considered redundant because they are too frequent, and meaningless once the word order is removed.
'''

# A set is a list with unique words
stopwords = set()

# define list of filtered words
filtered_words = []

# read stopwords from file & save them in a list
# read from file
with open("english.txt", "r") as source:
	# for each line
	for line in source:
		# clean returns
		line = line.strip()
		# add word to set stopwords (cfr difference with list: list.append())
		stopwords.add(line)

# define your sentence / string
sentence = 'I was at Synesthésie last night and took a bus to go home.'

# print sentence
print("phrase originale:", sentence)

# convert string to list of words
words = sentence.split(" ")
# for each word of list, check if word is in stopwords, if it isn't, add word to filtered wordlist
for word in words:
	if word not in stopwords:
		filtered_words.append(word)

# this is the same, but shorter + no need to declare filtered_words as list in the beginning:
#filtered_words = [word for word in words if word not in stopwords]



# turn wordlist into string of characters
new_sentence = " ".join(filtered_words)
# print new sentence
print("phrase réécrite:", new_sentence)




