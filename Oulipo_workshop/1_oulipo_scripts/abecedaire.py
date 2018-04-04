#!/usr/bin/python
# this is a shebang: https://en.wikipedia.org/wiki/Shebang_%28Unix%29

'''
This script takes a sentence you write in the terminal, and gives it back in alphabetical order
Check out other options for list comprehension: https://docs.python.org/3/tutorial/datastructures.html
Made for OLA #5, Paris, 15-17 décembre 2017
'''

# Run script in loop:
while True:

	# Ask to write a sentence
	sentence = input("Ecrivez votre phrase: ").lower().strip('\., \?')

	# Split sentence into words
	words = sentence.split()
	#print(words)

	# sort wordlist
	words.sort()
	print(" ".join(words).capitalize(), '.')

