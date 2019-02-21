import numpy as np
import nltk
import re
import collections
import string
#from nltk import words_tokenize

def parse_to_tokens(corpus):
	tokens = corpus.split()
	return tokens
	
def read_file():
	file = open("corpus.txt", "r")
	return file
	

def compute_unigram_probability():
	file = read_file()
	string = file.read()
	ngram_count = {}
	
	tokenized = parse_to_tokens(string)
	
	for tokens in tokenized:
		if not ngram_count or tokens not in ngram_count.keys():
			ngram_count[tokens] = 1
		elif tokens in ngram_count.keys():
			ngram_count[tokens] += 1
	
	vocabulary_count = len(ngram_count.keys())
	
	for key in ngram_count.keys():
		ngram_count[key] /= vocabulary_count
	print(ngram_count)
	
compute_unigram_probability()