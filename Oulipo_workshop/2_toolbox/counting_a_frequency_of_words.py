#!/usr/bin/env/ python

# This script creates a sorted frequency dictionary with stopwords.

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
from collections import Counter
import string
from nltk.corpus import stopwords


# VARIABLES


# textfiles
source1 = open('../data/1984_fragment.txt', 'rt')
source2 = open('../data/verne_fragment.txt', 'rt')
destination1 = open('../data/counting_1984.txt', 'wt')
destination2 = open('../data/counting_verne.txt', 'wt')


# FUNCTIONS

# PREPROCESSING TEXT FILE
## remove caps + breaks + punctuation
def remove_punct(f):
	tokens = (' '.join(line.replace('\n', '') for line in f)).lower()
	for c in string.punctuation:
		tokens= tokens.replace(c,"")
		tokens = tokens.strip()
		#print("tokens", type(tokens))
	return tokens

## create frequency dictionary 
def freq_dict(tokens):
	tokens = tokens.split(" ")
	frequency_d = {}
	# tokens = tokens.split(" ")
	for token in tokens:
		try:
			frequency_d[token] += 1
		except KeyError:
			frequency_d[token] = 1
	return frequency_d

## sort words by frequency (import module)
def sort_dict(frequency_d):
	c=Counter(frequency_d)
	frequency = c.most_common()
	return frequency

# write words in text file 
def write_to_file(frequency, g):
	for key, value in frequency:
		g.write(("{} : {} \n".format(key, value)))
	g.close()


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


# SCRIPT

# execute functions

tokens1 = remove_punct(source1)
tokens2 = remove_punct(source2)

frequency_d1 = freq_dict(tokens1)
frequency_d2 = freq_dict(tokens2)

frequency1 = sort_dict(frequency_d1)
frequency2 = sort_dict(frequency_d2)

# Write in textfile

write_to_file(frequency1, destination1)
write_to_file(frequency2, destination2)

source1.close()
source2.close()

destination1.close()
destination2.close()



