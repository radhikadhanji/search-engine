import sqlite3

#connection = sqlite3.connect('searchengine.db')
#c = connection.cursor()
#c.execute('''SELECT * FROM backlinks''')
#print(c.fetchone())
#connection.close()

#Example implementation of the indexer algorithm with some arbitrary documents

doc1 = "I really like cats, they are very cool."
doc2 = "Dogs and cats don't get along with each other."

tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()

#Tokens will be combined into a list of unique terms.
terms = list(set(tokens1 + tokens2))

inverted_index = {}

#For each term, find which documents contain it
for term in terms:
    documents = []
    if term in tokens1:
        documents.append("Document 1")
    if term in tokens2:
        documents.append("Document 2")
    #Show us which documents the word appears in 
    inverted_index[term] = documents

#Print all the terms with their words
for term, documents in inverted_index.items():
    print(term, "->", ", ".join(documents))