#!/usr/bin/env python
# Filename: file.py
# -*- coding: utf-8 -*-

class FileHandler:
	def load_file(self, filename):
		f = open(filename, 'r')
		return f.read()

if __name__ == '__main__':
	handler = FileHandler()
	print handler.load_file('test.txt')

# End of file.py