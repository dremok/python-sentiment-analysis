#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filehandler import *
from featurehandler import *

if __name__ == '__main__':
	file_handler = FileHandler(Structurizer())
	features = file_handler.load_all_tokens({'posTrain', 'negTrain'})
	feature_handler = FeatureHandler(features)
	
	valid_words = file_handler.load_word_lists()
	feature_handler.keep_only_these_words(valid_words)

	file_handler.set_output_file('train.arff')
	file_handler.write_all_instances(['posTrain', 'negTrain'], feature_handler, 'arff')

	file_handler.set_output_file('test.arff')
	file_handler.write_all_instances(['pos', 'neg'], feature_handler, 'arff')