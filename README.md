Sentiment
=========

Python project for doing "Sentiment Analysis" on text.
So far, it includes one module for finding structure in the text,
one for tokenizing and one for handling features (remove stop words etc.).

I have implemented functionality for reading positive and negative texts
and producing structured training files in .arff and LIBSVM formats.

It has been tested using logistic regression and SVM on some of the free review
corpuses on the net. The results were pretty good.

Next step:
==========
1. Finish a web crawler (implemented using the Scrapy library) that scrapes blog posts.
2. Manually annotate a couple of hundred posts.
3. Estimate sentiment on huge amounts of posts for a company (or product) over a period of time,
say a month. Compare to some hard figures, stock market price, sales figures etc.
