#!/usr/bin/python
# this is a shebang: https://en.wikipedia.org/wiki/Shebang_%28Unix%29

'''
This script looks at each word in a given text, if the word contains the letters of Perec, the word is printed to another textfile
Made for OLA #5, Paris, 15-17 décembre 2017
'''

# import external modules
import re
import string

# define textfiles
source = open("../data/1984_all.txt", 'r')
destination = open("../data/perec.txt", 'w')

# define regular expression
regex = r'(\w*p+\w*e+\w*r+\w*e+\w*c+)'


# write title to destination
destination.write("Source: George Orwell's 1984\n\n\n")

# search for pattern in source, print in terminal & write to destination
sentences = []
# read source line by line
for line in source:
	# split each line into list of words, split on white spaces
	words = line.split(" ")
	for word in words:
		# look if pattern is in word
		if re.search(regex, word):
			# if yes, print word in terminal
			print(word)
			# write word to file without punctuation
			destination.write(word.strip('\., \,')+'\n')

# close textfiles
source.close()
destination.close()