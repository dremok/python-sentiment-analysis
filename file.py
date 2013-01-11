#!/usr/bin/env python
# Filename: file.py
# -*- coding: utf-8 -*-

from __future__ import division

from token import *
from structure import *

class FileHandler:
	def load_file(self, filename):
		with open(filename, 'r') as f:
			read_text = f.read()
		f.close()
		return read_text

	def all_tokens(self, attitude):
		tok = Tokenizer()
		struc = Structurizer()
		i = 1
		tokens = set()
		while True:
			try:
				text = self.load_file(attitude + str(i) + ".txt")
				tokens = tok.tokenize(text)
				tokens = struc.negate(all_tokens)
				i = i + 1
			except:
				return set(tokens)

	def text2token_probs(self, text):
		probs = {}
		tok = Tokenizer()
		struc = Structurizer()
		tokens = tok.tokenize(text)
		tokens = struc.negate(tokens)
		for t in tokens:
			if t in probs:
				probs[t] = probs[t] + 1
			else:
				probs[t] = 1
		total_nbr_tokens = sum(probs.values())
		for token in probs:
			probs[token] = probs[token] / total_nbr_tokens
		return probs


if __name__ == '__main__':
	handler = FileHandler()
	all_tokens = handler.all_tokens('pos')
	text = handler.load_file('pos2.txt')
	probs = handler.text2token_probs(text)

# End of file.py