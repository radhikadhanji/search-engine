import sqlite3

#connection = sqlite3.connect('searchengine.db')
#c = connection.cursor()
#c.execute('''SELECT * FROM backlinks''')
#print(c.fetchone())
#connection.close()

#Example implementation of the inverted indexer algorithm with some arbitrary documents.

doc1 = "I really like cats they are very cool."
doc2 = "Dogs and cats don't get along with each other."

tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()

#Tokens will be combined into a list of unique terms.
terms = list(set(tokens1 + tokens2))

inverted_index = {}

#For each term, count the occurrences of the word
for term in terms:
    occurrence = 0
    if term in tokens1:
        occurrence+=1
    if term in tokens2:
        occurrence+=1
    #Assign each word to how much it occurs in the text
    inverted_index[term] = occurrence

#Print all the terms with their occurences
for term, occurrence in inverted_index.items():
    print(term, "->", occurrence)