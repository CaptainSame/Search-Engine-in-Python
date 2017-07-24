import sys
import os
import operator
import math
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer

def tokenise_normalise(raw_string):

#tokenize and normalise a string.

	tokenizer = RegexpTokenizer(r'\w+')
	tokenised_text = tokenizer.tokenize(str(raw_string))

	token_normalise = []
	for w in tokenised_text:
				
		w = w.lower()
		
		token_normalise.append(w)
	
	return token_normalise
	
def stem(token_normalised_text):

#stems a normalised tokens list.

	processed_text = []
	stemmer = PorterStemmer()

	for w in token_normalised_text:
				
		root = stemmer.stem(w)
		root = str(root)
		
		processed_text.append(root)
	
	return processed_text
	
	
def create_tf_dict_doc(processed_text, f, stats_dict):
		
#create a term-frequency dictionary for one document.
		
	for root in processed_text:
	
		if root not in stats_dict:
			
			stats_dict[root] = {}
			stats_dict[root][f] = 1
		
		if f not in stats_dict[root]:
			stats_dict[root][f] = 1
			
		stats_dict[root][f] += 1
		
	return stats_dict
		
def create_tf_dict_query(processed_query):

#creates tf-idf scores dictionary for query.
	query_dict = {}
	for root in processed_query:
		
		if root not in query_dict:
			
			query_dict[root] = 1
			
		query_dict[root] += 1
		
	return query_dict
		
		
def find_tfidf_doc(stats_dict, Number_of_docs):

#find idf scores for terms and update the tf-idf values in dictionary.
	
	idf_dict = {}
	for word in stats_dict:
		idf_dict[word] = len(stats_dict[word].keys())
		
	for word in stats_dict:
		for doc in stats_dict[word]:
			stats_dict[word][doc] = (1 + math.log(stats_dict[word][doc]))*math.log(Number_of_docs/idf_dict[word])

	return stats_dict, idf_dict
	
def find_tfidf_query(query_dict, idf_dict, Number_of_docs):

#find tf-idf scores for terms in query and returns a dictionary.

	for word in query_dict:
		query_dict[word] = (1 + math.log(query_dict[word]))*math.log(Number_of_docs/idf_dict[word])

	return query_dict
	



		
