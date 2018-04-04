#!/usr/bin/env/ python

# This script rewrites the novel by replacing the name of the principal 
# character in the novel by another name.  
# It writes the new version of novel to a file called starring_me.txt and to a Logbook in Context
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
			sys.stdout.write('%s' % char)
			sys.stdout.flush()
			time.sleep(0.1)
		sys.stdout.write(" ")
		sys.stdout.flush()

# write to file
def archive(sentence):
	with open("novel_starring_you.txt", "a") as destination:
		destination.write(sentence)

# loop script
while True:

	# introduction, getting the variables
	print("\n\t\tDear visitor, we will rewrite the opening scene of ", green("Kurt Vonnegut's 2BRO2B"), " using your name and favourite city.\n")
	#time.sleep(2)
	first_name = input("\t\tPlease type your first name: ")
	#time.sleep(2)
	last_name = input("\n\t\tPlease type your last name: ")
	#time.sleep(2)
	country = input("\n\t\tChoose a country: ")
	#time.sleep(2)
	city = input("\n\t\tChoose a city in that country: ")
	#time.sleep(2)
	print("\n\t\tDo you want to be", green('female'), "or", green('male?'))
	gender = input("\t\tPlease type f or m: ")
	#time.sleep(5)
	print("\n")

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
	time.sleep(10)

