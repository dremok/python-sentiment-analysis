#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filehandler import *

if __name__ == '__main__':
	handler = FileHandler(Structurizer())

	features = list(handler.all_tokens({'pos', 'neg'}))
	
	handler.write_relation_name("sentiment")
	handler.write_feature_names(features)
	handler.write_data_header()
	handler.write_all_training_data_for_label('pos', features)
	handler.write_all_training_data_for_label('neg', features)