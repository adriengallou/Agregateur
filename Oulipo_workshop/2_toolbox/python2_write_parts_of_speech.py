#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this script works in Python2

from __future__ import division
import nltk
from pattern.en import tag
import nltk.data
from random import shuffle, choice


# VARIABLES


# texts
source = open("../data/1984_fragment.txt", "r")
destination = open("../data/1984_fragment_pos.txt", "wt")
destination.write("1984\S SYNTAX using PENN'S TREEBANK\n\n")



# FUNCTIONS

## SCRIPT

# select 1 or more sentences from source
## split source text into list of sentences
finding_sentences = nltk.data.load('tokenizers/punkt/english.pickle')
sentences_list = []
with source as text0:
    for line in text0:
        # this returns a list with 1 element containing the entire text, sentences separated by \n
        sentences = '\n'.join(finding_sentences.tokenize(line.decode('utf-8').strip()))
        # transform string into list of sentences
        sentences_list = sentences.split("\n") 
        print("sentences list", sentences_list)

with destination as text1:
	for sentence in sentences_list:
	# create tuple of tuples with pairs of word + POS-tag
		collection = tag(sentence, tokenize=True, encoding='utf-8')
	# transform tuple into list to be able to manipulate it
		collection = list(collection)
		for element in collection:
			text1.write(element[1] + " ")
	