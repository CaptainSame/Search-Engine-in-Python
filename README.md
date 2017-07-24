# Search-Engine-in-Python
**ARMADAS Search Engine** Created By: Sameer Sharma.

Python 2.7 should be installed on a pc to run this project.
Python's NLTK library should be installed.
Python's Numpy library should be installed.
Python's PyEnchant library should be installed.
Python's Tkinter library should be installed.
WordNet should be downloaded from nltk.corpus.

The folder named "corpus" should contain all the text documents to be searched.

The program can be executed in two modes:
1. Using retrieval.py execution (command line interface)
2. Using gui.py execution (graphic user interface). GUI supports hyperlink feature for opening result documents.

# DESCRIPTION
**OVERVIEW**
The search engine employs vector space model for query searching in a text corpus, which uses proximity searching of query vector with individual document vectors to rank the documents according to relevance. The weight vectors formulated for this purpose use combination of term frequency and inverse document frequency scores. The proximity searching technique used is cosine similarity. The pre-processing of text in documents as well as the query is done using various Python libraries. The pre-processing includes tokenization, normalization and stemming of words. Spellchecking has also been employed for query input words. Synonym search is yet another feature employed by the application. Finally, a GUI interface has been created for the application for ease of searching.

**TOOLS USED**
The tokenizer used is RegexpTokenizer from Python’s NLTK Library. The normalized words are stemmed using Porter’s Stemming algorithm which is imported from Python’s NLTK library. The logarithmic formulas for term frequency and inverse document frequency are used to create the final dictionary of tf-idf scores. GUI frame has been created using Tkinter GUI library.

**QUERY SEARCH**
After tokenizing and normalizing the query, spellcheck is done. Enchant library of Python is used to suggest closest meaningful word to the user through a GUI message box. If the user approves the suggestion, the new term is added to the query list. Now, for each word in the query, its two most relevant synonyms are added to the query vector to enhance search results. The library used for this purpose is WordNet from nltk corpus. Finally, vectors are created for query and each document having tf-idf scores. Top 20 results are finally displayed after ranking through a Tkinter window and the result documents can be accessed by the links shown in the window.
