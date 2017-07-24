import enchant
from nltk.corpus import wordnet as wn

def spell_check(string):
#checks the spelling mistakes for each word and returns suggestions.
	checker = enchant.Dict("en_UK")
	error_dict = {}
	
	for w in string:
		
		if(checker.check(w)==False):
			if w not in error_dict:
				error_dict[w] = checker.suggest(w)[0].lower() 
		
	return error_dict
	
def synonym_list(processed_query):
#returns final query after adding relevant synonyms.
	final_query_words = []
	for w in processed_query:
	
		syns = wn.synsets(w)
		names=[s.name().split('.')[0] for s in syns]

		if len(names)>=2:names=names[:2]
		names.append(w)
		for n in names:
			final_query_words.append(n)
			
	return final_query_words
