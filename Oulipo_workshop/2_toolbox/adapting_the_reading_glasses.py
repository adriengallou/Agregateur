#!/usr/bin/env/ python
# THIS SCRIPT ADAPTS THE SOURCE TEXT IN THE RIGHT READING FORMAT FOR THE ALGORITHM, CLEANING UP WHITE SPACES/SPLITTING INTO SENTENCES
# source text is written in uppercase
# remove white spaces, put everything in lowercase
# split on punctuation
# write in file capitalizing first letter

 #    Copyright (C) 2016 Constant, Algolit, An Mertens

 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details: <http://www.gnu.org/licenses/>.


import nltk.data

# split into sentences
sentences = []
finding_sentences = nltk.data.load('tokenizers/punkt/english.pickle')
with open('../data/frankenstein_for_machines.txt', 'rt') as source:
	for line in source:
		# this returns a list with 1 element containing the entire text, sentences separated by \n
		sentences = '\n'.join(finding_sentences.tokenize(line.strip().lower().capitalize()))
		# transform string into list of sentences
		sentences = sentences.split("\n")

# write clean text to a file
with open("frankenstein_for_machines_tf.txt", "w") as destination:
	for sentence in sentences:
		destination.write(sentence.strip().capitalize()+" ")


