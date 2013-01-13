#!/usr/bin/env python
# self.output_file: featurehandler.py
# -*- coding: utf-8 -*-

import operator
from filehandler import *

class FeatureHandler:

	def __init__(self, features):
		self.features = features

	def keep_only_these_words(self, words):
		keep = {}
		for f in self.features:
			if (f in words) or (f[-4:] == "_NEG" and f[:-4] in words):
				keep[f] = self.features[f]
		self.features = keep

	def remove_most_common_words(self, alpha):
		nbr_to_remove = int(alpha * len(self.features))
		for i in range(1, nbr_to_remove):
			most_common_feature = max(self.features.iteritems(), key=operator.itemgetter(1))[0]
			del self.features[most_common_feature]


# Main function for testing purposes.
if __name__ == '__main__':
	file_handler = FileHandler(Structurizer())
	features = file_handler.load_all_tokens({'pos', 'neg'})
	fh = FeatureHandler(features)
	print len(features)
	fh.remove_most_common_words(0.2)
	print len(features)

# End of featurehandler.py