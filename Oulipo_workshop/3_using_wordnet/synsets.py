#!/usr/bin/env python
# coding: utf8

# More options with Wordnet: http://www.nltk.org/howto/wordnet.html

from nltk.corpus import wordnet as wn

print([synset.lemma_names('fra') for synset in wn.synsets('chien', lang='fra')])

'''
[['canis_familiaris', 'chien'], ['aboyeur', 'chien', 'chienchien', 'clébard', 'toutou'], ['chien', 'chien_de_chasse'], ['chien'], ['chien', 'clic', 'cliquer', 'cliquet'], ['chien', 'franc', 'hot-dog'], ['achille', 'chien', 'quignon', 'talon'], ['chien'], ['chien']
'''