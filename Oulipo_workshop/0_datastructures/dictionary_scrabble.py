#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) 2017 Constant, Algolit
 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details: <http://www.gnu.org/licenses/>.


'''
Input texts are checked against a dictionary that assigns weights to different vowels.
The script gives a score for a specific sentence.
'''

# create a dictionary
scrabble = {'a': 3, 'e': 1, 'i': 2, 'o': 4, 'u':4, 'y': 6}

# set weight to 0
weights = 0

# find a sentence / string
sentence = "La vie est un mystère qu'il faut vivre, et non un problème à résoudre."

# split sentence in list of words
words = sentence.split()

# for each word
for word in words:
	# iterate over letters of word
	for letter in word:
		# check if letter is in dictionary
		if letter in scrabble:
			# if yes, get weight of the letter
			weight = scrabble[letter]
			# add letter weight to general weight
			weights += weight

# print general weight
print("Le poids de ma phrase est:", weights)
