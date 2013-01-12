#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure import *
from token import *

if __name__ == '__main__':
	tok = Tokenizer()
	struc = Structurizer()
	
	words = tok.tokenize(test)
	words = struc.negate(words)

	print "\n".join(words)