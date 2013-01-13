#!/usr/bin/env python
# Filename: structure.py
# -*- coding: utf-8 -*-

from __future__ import division
import re
from token import *

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
punct_re = re.compile(r"^[\s/_\-.,:;!?\d]+(_NEG)?$", re.VERBOSE | re.I | re.UNICODE)
apostrophes_re = re.compile(r"['\"%]+", re.VERBOSE | re.I | re.UNICODE)

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

	def remove_punctuation_etc(self, words):
		return filter(lambda x:punct_re.match(x) is None and len(x) > 0, words)

	def remove_apostrophes_etc(self, words):
		return map(lambda x:apostrophes_re.sub('', x), words)

	def text2bag_of_words(self, text):
		tok = Tokenizer()
		tokens = tok.tokenize(text)
		tokens = self.negate(tokens)
		tokens = self.remove_punctuation_etc(tokens)
		tokens = self.remove_apostrophes_etc(tokens)
		return tokens

	def text2freqs(self, text):
		freqs = {}
		tokens = self.text2bag_of_words(text)
		for t in tokens:
			if t in freqs:
				freqs[t] = freqs[t] + 1
			else:
				freqs[t] = 1
		total_nbr_tokens = sum(freqs.values())
		for token in freqs:
			freqs[token] = freqs[token] / total_nbr_tokens
		return freqs


# Main function for testing purposes.
if __name__ == '__main__':
	tok = Tokenizer()
	struc = Structurizer()
	print punct_re.match("")
	# words = struc.text2bag_of_words("it's a shining day isn't it?")
	# print "\n".join(words)
	# words = struc.negate(words)
	# words = struc.remove_punctuation_etc(words)
	
	# print "\n".join(words)
	# print words

# End of structure.py