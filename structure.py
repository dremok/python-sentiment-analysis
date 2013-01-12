#!/usr/bin/env python
# Filename: structure.py
# -*- coding: utf-8 -*-

import re

from token import *

test = "I am thinking about buying the new iPhone. Looks really cooooool :D Samsung Galaxy is not nearly as cool IMHO!"

neg_str = r"""
	(?:
    	^(?:never|no|nothing|nowhere|noone|none|not|
        	havent|hasnt|hadnt|cant|couldnt|shouldnt|
        	wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint
    	)$
	)
	|
	n't
	"""

neg_re = re.compile(neg_str, re.VERBOSE | re.I | re.UNICODE)
clausePunct_re = re.compile(r"^[.:;!?]$", re.VERBOSE | re.I | re.UNICODE)
notPunct_re = re.compile(r"^[.:;!?]$", re.VERBOSE | re.I | re.UNICODE)

class Structurizer:
	def negate(self, words):
		neg = False
		for i in range(len(words)):
			w = words[i]
			if neg == False:
				if neg_re.search(w):
					neg = True
			else:
				if clausePunct_re.search(w):
					neg = False
				else:
					words[i] = w + "_NEG"
		return words

	def remove_punctuation(self, words):
		return filter(lambda x:clausePunct_re.match(x) is None, words)
				

if __name__ == '__main__':
	tok = Tokenizer()
	struc = Structurizer()
	
	words = tok.tokenize(test)
	words = struc.negate(words)
	words = struc.remove_punctuation(words)
	
	print "\n".join(words)
	# print words

# End of structure.py