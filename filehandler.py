#!/usr/bin/env python
# self.output_file: filehandler.py
# -*- coding: utf-8 -*-

from __future__ import division
import glob
import sys
from structure import *
from featurehandler import *

class FileHandler:
	output_file = "train.arff"

	def __init__(self, struc):
		self.struc = struc

	def set_output_file(self, filename):
		self.output_file = filename

	def load_all_tokens(self, labels):
		all_tokens = {}
		for label in labels:
			for filename in glob.glob("reviews/" + label + "/*.txt"):
				with open(filename) as f:
					text = f.read()
					tokens = self.struc.text2bag_of_words(text)
					for t in tokens:
						if t in all_tokens:
							all_tokens[t] = all_tokens[t] + 1
						else:
							all_tokens[t] = 1
				f.close()
		return all_tokens

	def load_word_lists(self):
		words = []
		for filename in glob.glob("words/*.csv"):
			with open(filename) as f:
				words.extend(f.read().split())
		for filename in glob.glob("words/*.txt"):
			with open(filename) as f:
				words.extend(f.read().split())
		return set(map(lambda x:x.lower(), words))

	def write_relation_name(self, relation, filetype):
		if filetype == 'arff':
			with open(self.output_file, 'a') as f:
				f.write("@RELATION " + relation + "\n\n")
			f.close()
		else:
			print 'Unrecognized filetype.'
			sys.exit(1)

	# features must be a list
	def write_feature_names(self, features, filetype):
		if filetype == 'arff':
			with open(self.output_file, 'a') as f:
				for i in range(0, len(features)):
					f.write("@ATTRIBUTE " + features[i] + " NUMERIC\n")
				f.write("@ATTRIBUTE CLASS_LABEL {pos,neg}\n")
			f.close()
		else:
			print 'Unrecognized filetype.'
			sys.exit(1)			

	def write_data_header(self, filetype):
		if filetype == 'arff':
			with open(self.output_file, 'a') as f:
				f.write("\n@DATA\n")
			f.close()
		else:
			print 'Unrecognized filetype.'
			sys.exit(1)
		
	def write_training_data(self, label, features, freqs, filetype):
			with open(self.output_file, 'a') as f:
				if filetype == 'libsvm':
					if label == 'pos':
						f.write('+1 ')
					elif label == 'neg':
						f.write('-1 ')
				for i in range(0, len(features)):
					feat = features[i]
					if feat in freqs:
						if filetype == 'arff':
							f.write(str(freqs[feat]) + ",")
						elif filetype == 'libsvm':
							f.write(str(i) + ":" + str(freqs[feat]) + " ")
					else:
						if filetype == 'arff':
							f.write("0,")
				if filetype == 'arff':
					if 'pos' in label:
						f.write('pos' + "\n")
					elif 'neg' in label:
						f.write('neg' + "\n")
				elif filetype == 'libsvm':
					f.write("\n")
			f.close()

	def write_all_instances(self, labels, feature_handler, filetype):
		if filetype == 'arff':
			self.write_relation_name("sentiment", 'arff')
			self.write_feature_names(list(feature_handler.features), 'arff')
			self.write_data_header('arff')
		for label in labels:
			for filename in glob.glob("reviews/"+ label + "/*.txt"):
				with open(filename) as f:
					text = f.read()
					freqs = self.struc.text2freqs(text)
					self.write_training_data(label, list(feature_handler.features), freqs, filetype)
				f.close()


# Main function for testing purposes.
if __name__ == '__main__':
	handler = FileHandler(Structurizer())
	features = handler.load_all_tokens({'pos', 'neg'})
	handler.write_all_training_data(list(features.keys()), 'arff')
	
	# handler.write_all_training_data('pos', features, 'arff')
	# handler.write_all_training_data('neg', features, 'arff')

# End of filehandler.py