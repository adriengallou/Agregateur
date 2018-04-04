import re


source = open("../data/1984_fragment.txt", "r")
#source = open("joyce.txt", "r")
destination = open("../data/1984_no_digits.txt", "w")


sentences = []
for line in source:
	result = ''.join([i for i in line if not i.isdigit()])
	destination.write(result)

source.close()
destination.close()