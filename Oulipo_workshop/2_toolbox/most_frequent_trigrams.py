from collections import Counter
import nltk
import re
import pickle


# VARIABLES

source = open("../data/1984_fragment.txt", "r")
destination = open("../data/1984_fragment_trigrams.txt", "w")
destination.write("OBAMA\S MOST FREQUENT TRIGRAMS with Penn's TREEBANK\n\n\n")


# FUNCTIONS
## sort words by frequency (import module)
def sort_dict(frequency_d):
	c=Counter(frequency_d)
	frequency = c.most_common()
	return frequency

## MAKE SURE ALL VARIABLES ARE DECLARED WITHIN THE LOOPS		

# 1. Create dictionary of trigrams
trigrams = {}
for line in source:
	# remove punctuation
	clean_tri = []
	words = line.split(" ")
	for word in words:
		cleaning = re.compile(r"[A-Za-z0-9]")
		if cleaning.match(word):
			clean_tri.append(word)
		else:
			pass
	# find trigrams
	tricount = nltk.trigrams(clean_tri)	
	# count frequency of each trigram and add trigram + value in dictionary			
	for trigram in tricount:
		if trigram in trigrams:
			trigrams[trigram] += 1
		else:
			trigrams[trigram] = 1	

trigrams_sorted = sort_dict(trigrams)
first10pairs = trigrams_sorted[:10]


with destination as text:
	for tri, frequency in first10pairs:
		text.write("{} : {} \n".format(tri, frequency))




