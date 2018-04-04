#!/usr/bin/env/ python

# This script makes you choose 1 out of 2 Oulipo constraints:

# Constraint 1: http://oulipo.net/fr/contraintes/litterature-definitionnelle
# Constraint 2: rewrites the beginning of a novel by replacing the principal names/places/gender
# The idea for this script comes from the book 'Think Python'.

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
from random import shuffle, choice, randrange

import colors
from colors import red, green, yellow, blue, magenta, cyan, bold, underline
import time
import os, sys


## FUNCTIONS
# print on screen character per character
def typewrite(sentence):
	words = sentence.split(" ")
	for word in words:
		for char in word:
			if char != "<" and char != ">":
				sys.stdout.write('%s' % char)
				sys.stdout.flush()
				time.sleep(0.1)
		sys.stdout.write(" ")
		sys.stdout.flush()

# loop script
while True:

	print "\n\t\tDear visitor, you can choose between", red(" two Oulipo applications.\n")
	#source = open("frankenstein_for_machines.txt", 'r')
	print "\t\tOption a is ", green("Litterature Definitionnelle"), " with sentences from Mary Shelley's Frankenstein.\n"
	#source = open("frankenstein_for_machines.txt", 'r')
	print "\t\tOption b is ", green("A Novel Starring You.\n")
	#source = open("frankenstein_for_machines.txt", 'r')
	print "\t\tType ", green('a'), " if you want to play with Litterature Definitionnelle.\n"
	#source = open("frankenstein_for_machines.txt", 'r')
	print "\t\tType ", green('b'), " if you want to be a star in the opening scene of Kurt Vonneguts' 2BRO2B.\n"
	#source = open("frankenstein_for_machines.txt", 'r')
	choice = raw_input("\t\tYour choice is: ")
	#source = open("frankenstein_for_machines.txt", 'r')
	print "\n"

	os.system('cls' if os.name == 'nt' else 'clear')
	print "\n"


### MEET ---------------------------------------------------------------------------------------------
### --------------------------------------------------------------------------------------------------

### MEET/INTRO ---------------------------------------------------------------------------------------------

	# retrain model
	if choice == 'a':

		### Litterature definitionnelle

		# textfiles
		source = open("frankenstein_for_machines.txt", 'r')
		#source = open("1984_fragment.txt", 'r')
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
		  
		selected_sentences = [sentences_list[randrange(len(sentences_list))]
              for s in range(4)]

		

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
		#print " ".join(definitions)
		for d in definitions:
			typewrite(d)

		raw_input("\nPress Enter to continue...")
		# time.sleep(10)

		# -------------------------------------------

	elif choice == 'b':

		### A Novel Starring You

		# introduction, getting the variables
		print "\n\t\tDear visitor, we will rewrite the opening scene of ", green("Kurt Vonnegut's 2BRO2B"), " using your name and favourite city.\n"
		##source = open("frankenstein_for_machines.txt", 'r')
		first_name = raw_input("\t\tPlease type your first name: ")
		##source = open("frankenstein_for_machines.txt", 'r')
		last_name = raw_input("\n\t\tPlease type your last name: ")
		##source = open("frankenstein_for_machines.txt", 'r')
		country = raw_input("\n\t\tChoose a country: ")
		##source = open("frankenstein_for_machines.txt", 'r')
		city = raw_input("\n\t\tChoose a city in that country: ")
		##source = open("frankenstein_for_machines.txt", 'r')
		print "\n\t\tDo you want to be", green('female'), "or", green('male?')
		gender = raw_input("\t\tPlease type f or m: ")
		#time.sleep(5)
		print "\n"

		# specify input text
		source = open("vonnegut.txt", "r")
		sentences =[]
		
		# write & replace
		archive("\n\nNovel Starring You\n")
		archive("-------------\n\n")

		with source as text: 
			for line in text:
				line = line.replace("the United States", country)
				line = line.replace("Chicago", city)
				line = line.replace("Edward K.", first_name)
				line = line.replace("Wehling", last_name)
				if gender == 'f':
					line = line.replace(" man ", " woman ")
					line = line.replace(" man,", " woman,")
					line = line.replace(" his ", " her ")
					line = line.replace(" him ", " her ")
					line = line.replace(" His ", " Her ")
					line = line.replace(" wife ", " husband ")
					line = line.replace(" he ", " she ")
					line = line.replace(" He ", " She ")
				typewrite(line)
				archive(line)
		# break before relaunching the script
		raw_input("\nPress Enter to continue...")		
		time.sleep(10)

### ELSE --------------------------------------------------------------------------------------
### -------------------------------------------------------------------------------------------

	# try again
	else:
		print "\t\tYou must have typed something else."
		#time.sleep(30)
		raw_input("\nPress Enter to continue...")
		os.system('cls' if os.name == 'nt' else 'clear')
		