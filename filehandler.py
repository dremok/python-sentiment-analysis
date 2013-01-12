#!/usr/bin/env python
# self.output_file: filehandler.py
# -*- coding: utf-8 -*-

from __future__ import division
import glob

from structure import *

class FileHandler:
	output_file = "train.arff"

	def __init__(self, struc):
		self.struc = struc

	def all_tokens(self, labels):
		tokens = []
		for label in labels:
			for filename in glob.glob("reviews/" + label + "/*.txt"):
				with open(filename) as f:
					text = f.read()
					tokens.extend(self.struc.text2bag_of_words(text))
				f.close()
		return set(tokens)

	def write_relation_name(self, relation):
		with open(self.output_file, 'a') as f:
			f.write("@RELATION " + relation + "\n\n")
		f.close()

	def write_feature_names(self, features):
		with open(self.output_file, 'a') as f:
			for feature in features:
				f.write("@ATTRIBUTE " + feature + " NUMERIC\n")
			f.write("@ATTRIBUTE CLASS_LABEL {pos,neg}\n")
		f.close()

	def write_data_header(self):
		with open(self.output_file, 'a') as f:
			f.write("\n@DATA\n")
		f.close()

	def write_training_data(self, label, features, freqs):
		with open(self.output_file, 'a') as f:
			for feature in features:
				if feature in freqs:
					f.write(str(freqs[feature]) + ",")
				else:
					f.write("0,")
			f.write(label + "\n")
		f.close()

	def write_all_training_data_for_label(self, label, features):
		for filename in glob.glob("reviews/" + label + "/*.txt"):
			with open(filename) as f:
				text = f.read()
				freqs = self.struc.text2freqs(text)
				self.write_training_data(label, features, freqs)
			f.close()


# Main function for testing purposes.
if __name__ == '__main__':
	handler = FileHandler(Structurizer())

	features = list(handler.all_tokens({'pos', 'neg'}))
	
	handler.write_relation_name("sentiment")
	handler.write_feature_names(features)
	handler.write_data_header()
	handler.write_all_training_data_for_label('pos', features)
	handler.write_all_training_data_for_label('neg', features)

# End of filehandler.py