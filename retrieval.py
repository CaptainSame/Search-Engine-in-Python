import sys
import os
import operator
import numpy as np
import tokeniser as tkn
import spellcheck as sc

corpus_dir = "corpus"

#getting text files
text_files = [os.path.join(corpus_dir, f) for f in os.listdir(corpus_dir)]
stats_dict = {}

#getting number of docs
Number_of_docs = len(text_files)

doc_list = []

for f in text_files:
#reading each doc
	doc = open(f, 'r')
	lines = [l.strip() for l in doc.readlines()]

	index = 0 

	full_transcript = []

	while True:
		if index >= len(lines):
			break
		line = lines[index]
		full_transcript.append(line)
		index += 1

#tokenising and stemming text
	processed_text = tkn.tokenise_normalise(full_transcript)
	processed_text = tkn.stem(processed_text)
	stats_dict = tkn.create_tf_dict_doc(processed_text, f, stats_dict) #creating tf dictionary
	doc_list.append(f)
	
#creating dictionary with tf-idf scores	
stats_dict, idf_dict = tkn.find_tfidf_doc(stats_dict, Number_of_docs)

list_of_words = sorted(stats_dict.keys())
doc_list.sort()

option = "y"

while option=="y":
#getting the query input
	query = raw_input("Enter the query.\t")
	
	processed_query = tkn.tokenise_normalise(query) #normalising the query
	
	error_dict = sc.spell_check(processed_query) #checking query for spelling mistakes
	
	for w in error_dict:
	#suggest word for each spelling mistake.
		print "Did you mean", error_dict[w], "?"
		response = raw_input("(y/n)")
		
		if response=="y":
			for i,q in enumerate(processed_query):
				if q==w:
					processed_query[i]=error_dict[w]
				
	
	final_query = sc.synonym_list(processed_query) #adding most relevant synonyms to the query list
	
	final_query = tkn.stem(final_query) #stemming the query
	
	final_query = [x for x in final_query if x in stats_dict]
	if final_query!=[]:
		
		print final_query
			
		query_dict = tkn.create_tf_dict_query(final_query) #finding tf scores for each query word
	
		query_dict = tkn.find_tfidf_query(query_dict, idf_dict, Number_of_docs) #find tf-idf scores for each query word
			
		vector_array = np.zeros((len(query_dict.keys()), Number_of_docs))
	
		i=0
		j=0
	
		query_vector = np.zeros((1, len(query_dict.keys())))
	
		for w in query_dict:
		#create tf-idf vector for each document for each word in query
		
			query_vector[0][i] = query_dict[w]
			for d in doc_list:
				if d not in stats_dict[w]:
					j += 1
				else :
					vector_array[i][j] = stats_dict[w][d]
					j += 1
			i += 1
			j = 0
		
		magnitude = np.linalg.norm(vector_array, axis = 0) #changing the document vectors to unit vectors.
		vector_array = np.divide(vector_array, magnitude)
		vector_array[np.isnan(vector_array)] = 0
	
		q_magnitude = np.linalg.norm(query_vector, axis = 1) #changing the query vector to unit vector
		query_vector = np.divide(query_vector, q_magnitude)
	
		dot_product = np.dot(query_vector, vector_array) #finding the dot product of each document vector with query vector.
		dot_product = dot_product.tolist()
	
		final_rank = list(zip(dot_product[0], doc_list)) #sorting the cosine scores to rank the documents.
		final_rank.sort(reverse = True)
	
		for i in final_rank[:20]:
			print i[1]
	else:print 'OOPS! No Results Found' #if query is empty, print error message.
	option = raw_input("Do you want to continue.(y/n)") #asking the user to continue or not.
	
	
				
	
	
	
