#!/usr/bin/env/ python
# This script automatises the following Oulipo constraint: 
# http://oulipo.net/fr/contraintes/litterature-definitionnelle
# The output is printed in a txt-file and in a Logbook in Context

 #    Copyright (C) 2016 Constant, Algolit, An Mertens

 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details: <http://www.gnu.org/licenses/>.


from __future__ import division
import nltk
from nltk.corpus import wordnet as wn
from pattern.en import tag
import nltk.data
from random import shuffle, choice


# VARIABLES


# textfiles
source = open("frankenstein_for_machines.txt", 'r')
destination = open("litterature_definitionelle.txt", "wt")


## SCRIPT


# select 4 sentences from source
## split source text into list of sentences
finding_sentences = nltk.data.load('tokenizers/punkt/english.pickle')
sentences_list = []
with source as text:
    for line in text:
        # this returns a list with 1 element containing the entire text, sentences separated by \n
        sentences = '\n'.join(finding_sentences.tokenize(line.strip()))
        # transform string into list of sentences
        sentences_list = sentences.split("\n") 

# pick 4 random sentences
selected_sentences = []
number = 0
while number < 5:
	selected_sentences.append(choice(sentences_list))
	number += 1


# tokenize source and get Part-of-Speech tags for each word
definitions = []

for sentence in selected_sentences:
	# create tuple of tuples with pairs of word + POS-tag
	collection = tag(sentence, tokenize=True, encoding='utf-8')
	# transform tuple into list to be able to manipulate it
	collection = list(collection)
	# for each pair:
	for element in collection:
		# look for nouns & replace them with their definition
		if element[1] == "NN":
			if wn.synsets(element[0]):
				synset = wn.synsets(element[0])
				definitions.append("<")
				definitions.append(synset[0].definition())
				definitions.append(">")
			else:
				break
		else:
			# non-nouns are left as words
			definitions.append(element[0])


# write the transformed sentence
#print(" ".join(definitions))
with destination as text:
	text.write("ORIGINAL TEXT\n\n\n")
	for sentence in selected_sentences:
		text.write(sentence+"\n")
	text.write("\n\n")
	text.write("\n\nLITTERATURE DEFINITIONELLE\n\n\n")
	text.write(" ".join(definitions))

				
# close the text file
source.close()
destination.close()

# -------------------------------------------

# # Write in logbook

# # print chapters

# #writetologbook('\setuppagenumber[state=start]')     
# writetologbook('\n\section{LITTERATURE DEFINITIONELLE}\n')
# # print_sentences(spring_chapter)
# writetologbook('\nORIGINAL TEXT\crlf\crlf\n')
# for sentence in selected_sentences:
# 	writetologbook(sentence+"\n")
# writetologbook("\crlf\crlf\n\n\n")
# writetologbook('\nLITTERATURE DEFINITIONELLE\crlf\crlf\n')
# writetologbook(" ".join(definitions))