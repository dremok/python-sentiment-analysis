#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

emoticon_string = r"""
    (?:
      [<>]?						 # optional hat/brow
      [:;=8]                     # eyes
      [\-o\*\'\^]?               # optional nose
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth      
      |							 #### reverse orientation
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      [\-o\*\'\^]?               # optional nose
      [:;=8]                     # eyes
      [<>]?
    )"""

re_strings = (
	# Emoticons:
	emoticon_string,
	# Remaining words:
	r"""
	(?:[a-z][a-z'\-_]+[a-z])			# Words with apastrophes or dashes.
	|
	(?:[\w_]+)							# Words without apastrophes or dashes.
	|
	(?:[+\-\$]?\d+[,/.:-]\d+[+\-%]?)	# Numbers.
	|
	(?:\.(?:\s*\.){1,})					# Ellipsis dots.
	|
	(?:\S)								# Everything else that isn't whitespace.
	"""
	)

word_re = re.compile("|".join(re_strings), re.VERBOSE | re.I | re.UNICODE)
emoticon_re = re.compile(emoticon_string, re.VERBOSE | re.I | re.UNICODE)

class Tokenizer:
    def tokenize(self, text):
    	# Try to ensure unicode:
        try:
            text = unicode(text)
        except UnicodeDecodeError:
            text = str(text).encode('string_escape')
            text = unicode(text)
        words = re.findall(word_re, text)
        words = map((lambda x : x if emoticon_re.search(x) else x.lower()), words)
        return words

if __name__ == '__main__':
    tok = Tokenizer()
    words = tok.tokenize("Listen y'all.... Is this text tokenized, or what? :D Btw, I owe my mom $10!")
    print "\n".join(words)