#!/usr/bin/env python
# self.output_file: file.py
# -*- coding: utf-8 -*-

from __future__ import division
import glob

from token import *
from structure import *

class FileHandler:
	output_file = "train.arff"

	def read_file(self, input_file):
		with open(input_file, 'r') as f:
			read_text = f.read()
		f.close()
		return read_text

	def text2tokens(self, text):
		tok = Tokenizer()
		struc = Structurizer()
		tokens = tok.tokenize(text)
		tokens = struc.negate(tokens)
		tokens = struc.remove_punctuation(tokens)
		return tokens

	def all_tokens(self, label):
		tokens = []
		for filename in glob.glob("reviews/" + label + "/*.txt"):
			with open(filename) as f:
				text = f.read()
				tokens.extend(self.text2tokens(text))
		return set(tokens)

	def write_feature_names(self, features):
		with open(self.output_file, 'a') as f:
			for feature in features:
				f.write("@ATTRIBUTE " + feature + "\tNUMERIC\n")
			f.write("@ATTRIBUTE class\t{pos,neg}\n")
		f.close()

	def write_data_header(self):
		with open(self.output_file, 'a') as f:
			f.write("\n@DATA\n")
		f.close()

	def text2probs(self, text):
		probs = {}
		tok = Tokenizer()
		struc = Structurizer()
		tokens = self.text2tokens(text)
		for t in tokens:
			if t in probs:
				probs[t] = probs[t] + 1
			else:
				probs[t] = 1
		total_nbr_tokens = sum(probs.values())
		for token in probs:
			probs[token] = probs[token] / total_nbr_tokens
		return probs

	def write_training_data(self, label, features, probs):
		with open(self.output_file, 'a') as f:
			for feature in features:
				if feature in probs:
					f.write(str(probs[feature]) + ",")
				else:
					f.write("0,")
			f.write(label + "\n")
		f.close()

	def write_all_training_data_for_label(self, label, features):
		tok = Tokenizer()
		struc = Structurizer()
		for filename in glob.glob("reviews/" + label + "/*.txt"):
			with open(filename) as f:
				text = f.read()
				probs = self.text2probs(text)
				self.write_training_data(label, features, probs)


if __name__ == '__main__':
	handler = FileHandler()

	features = list(handler.all_tokens('pos'))
	features.extend(list(handler.all_tokens('neg')))
	handler.write_feature_names(features)
	handler.write_data_header()
	handler.write_all_training_data_for_label('pos', features)
	handler.write_all_training_data_for_label('neg', features)

# End of file.py