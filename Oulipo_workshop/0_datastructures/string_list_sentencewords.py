#!/usr/bin/env python
# encoding=utf8  

 #    Copyright (C) 2016 Constant, Algolit
 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details: <http://www.gnu.org/licenses/>.


# Reduction of letters
# From string to list & back
# A string: a list of characters, unchangeable, but treatable
# See: https://www.tutorialspoint.com/python3/python_strings.htm

# Write sentence as string
sentence = "Je vois La Vie en rose..."
# Print sentence
print("phrase originale:", sentence)

# define new word as list
new_word = []

# Convert sentence in list of words
words = sentence.split(" ")
# For each word in word list
for word in words:
	# remove capital letters (string operation)
	word = word.lower()
	# Clean punctuation (string operation)
	word = word.strip(" ;''?:,()!.\").”-")
	# add word to new word list
	new_word.append(word)

# Write words as one, without punctuation
print("phrase mise en mots:", ''.join(new_word))



