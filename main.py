#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filehandler import *
from featurehandler import *

if __name__ == '__main__':
	file_handler = FileHandler(Structurizer())
	features = file_handler.load_all_tokens({'pos', 'neg'})
	feature_handler = FeatureHandler(features)
	
	valid_words = file_handler.load_word_lists()
	feature_handler.keep_only_these_words(valid_words)

	features = feature_handler.features

	file_handler.write_relation_name("sentiment")
	file_handler.write_feature_names(features)
	file_handler.write_data_header()
	file_handler.write_all_training_data_for_label('pos', features)
	file_handler.write_all_training_data_for_label('neg', features)