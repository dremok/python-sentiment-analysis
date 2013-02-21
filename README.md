Sentiment
=========

Python project for doing "Sentiment Analysis" on text.
So far, it includes one module for finding structure in the text,
one for tokenizing and one for handling features (remove stop words etc.).

I have implemented functionality for reading positive and negative training data
and producing structured training files in .arff and LIBSVM formats.

It has been tested using Logistic regression and SVM on some of the free review
corpuses on the net. The results were quite good.

Next step:
==========
Finish a web crawler (implemented using the Scrapy library) that scrapes blog posts.
