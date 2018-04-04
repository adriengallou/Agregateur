#!/usr/bin/env/ python

# This script creates a sorted frequency dictionary with stopwords

 #    Copyright (C) 2016 Constant, Algolit, An Mertens

 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details: <http://www.gnu.org/licenses/>.



from collections import Counter
import string
import nltk



'''
This script creates a frequency dictionary of words used in a text filtering out stopwords
'''

# VARIABLES



# textfiles
source1 = open('../data/1984_fragment.txt', 'rt')
source2 = open('../data/verne_fragment.txt', 'rt')
destination1 = open('../data/grand_cru_counting_1984.txt', 'wt')
destination2 = open('../data/grand_cru_counting_verne.txt', 'wt')


freqwords = ["the", "a", "to", "of", "in", 'is', "with", "on", "for", "at", "from", "about",\
 "are", "an", "up", "out", "have", "be", "this", "one", "says", "as", "all", "just", "was", "so", "there", "not", "by",\
 "into", "been", "dont", "has", "over", "doesnt", "did", "had", "would", "could", "didnt"]
relationals = ["she", "you", "i", "he", "we", "her", "his", "it", "its", "their", "me", "our", 'they', "us", "my",\
"your", "theyre", 'them', "youre", "him", "were", "these"]
subphrases = ["and", "that", "but", "like", "what", "if", "then","theres", "or", "which", "who", "while", "where", "when",\
"thats", "how", "because"]

# removed "she", "you", "i", "he", "we",
stopwords = ["the", "a", "to", "of", "in", 'is', "with", "on", "for", "at", "from", "about",\
 "are", "an", "up", "out", "have", "be", "this", "one", "says", "as", "all", "just", "was", "so",\
 "her", "his", "it", "its", "their", "me", "our",\
 "and", "that", "but", "like", "what", "if", "then", "there", "they", "us", "my", "your", "theres", "theyre", "or", "not",\
 "which", "by", "who", "them", "into", "while", "been", "dont", "where", "youre", "has", "when", "over", "him", "were", "doesnt",\
 "did", "thats", "how", "had", "these", "would", "could", "because", "didnt"]


## FUNCTIONS

# PREPROCESSING TEXT FILE
## remove caps + breaks + punctuation
def remove_punct(f):
	tokens = (' '.join(line.replace('\n', '') for line in f)).lower()
	for c in string.punctuation:
		tokens= tokens.replace(c,"")
		tokens = tokens.strip()
		#print("tokens", type(tokens))
	return tokens

# remove stopwords
def remove_stopwords(tokens):
	tokens = tokens.split(" ")
	words =[]
	for token in tokens:
		if token not in stopwords:
			words.append(token)
	return words

## create frequency dictionary 
def freq_dict(words):
	frequency_d = {}
	# tokens = tokens.split(" ")
	for word in words:
		try:
			frequency_d[word] += 1
		except KeyError:
			frequency_d[word] = 1
	return frequency_d

## sort words by frequency (import module)
def sort_dict(frequency_d):
	c=Counter(frequency_d)
	frequency = c.most_common()
	return frequency

# write words in text file 
def write_to_file(frequency, destination):
	for key, value in frequency:
		destination.write(("{} : {} \n".format(key, value)))
	destination.close()


# Write new text into logbook
def writetologbook(content):
    try:
        log = open(filename, "a")
        try:
            log.write(content)
        finally:
            log.close()
    except IOError:
        pass


## SCRIPT

# execute functions
tokens1 = remove_punct(source1)
tokens2 = remove_punct(source2)

words1 = remove_stopwords(tokens1)
words2 = remove_stopwords(tokens2)

frequency_d1 = freq_dict(words1)
frequency_d2 = freq_dict(words2)

frequency1 = sort_dict(frequency_d1)
frequency2 = sort_dict(frequency_d2)

write_to_file(frequency1, destination1)
write_to_file(frequency2, destination2)

source1.close()
source2.close()

destination1.close()
destination2.close()

# -------------------------------------------
