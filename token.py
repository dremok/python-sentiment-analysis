#!/usr/bin/env python
# Filename: token.py
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

ellipsis_string = "(?:\.(?:\s*\.){1,})"

re_strings = (
	# Emoticons:
	emoticon_string,
    ellipsis_string,
	# Remaining words:
	r"""
    (?:[a-z][a-z'\-_]+[a-z])                # Words with apostrophes or dashes.
    |
    (?:[+\-$%]?\d+[,/.:-]?\d+[+\-$%]?)  # Numbers, including fractions, decimals.
    |
    (?:[\w_]+)                              # Words without apostrophes or dashes.
    |
    (?:\S)                                  # Everything else that isn't whitespace.
    """
    )

word_re = re.compile("|".join(re_strings), re.VERBOSE | re.I | re.UNICODE)
emoticon_re = re.compile(emoticon_string, re.VERBOSE | re.I | re.UNICODE)
ellipsis_re = re.compile(ellipsis_string, re.VERBOSE | re.I | re.UNICODE)
allCaps_re = re.compile("^(?:[^a-z][^a-z]+$)", re.VERBOSE | re.UNICODE)

class Tokenizer:
    def to_lower(self, words):
        return map((lambda x : x if (emoticon_re.search(x) or allCaps_re.search(x)) else x.lower()), words)

    def norm_repetition(self, words):
        return map((lambda x : re.sub(r"(.)\1{2,}", r"\1\1\1", x)), words)

    def tokenize(self, text):
    	# Try to ensure unicode:
        try:
            text = unicode(text)
        except UnicodeDecodeError:
            text = str(text).encode('string_escape')
            text = unicode(text)
        words = re.findall(word_re, text)
        words = self.to_lower(words)
        words = self.norm_repetition(words)

        return words

if __name__ == '__main__':
    tok = Tokenizer()
    words = tok.tokenize("Listen y'all.... Is this text tokenized, or what? :D BTW, precision can never be 100%. And I soooooooooo owe my CEO $10!")
    print "\n".join(words)

# End of token.py