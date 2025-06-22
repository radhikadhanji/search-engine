import sqlite3

connection = sqlite3.connect('searchengine.db')
c = connection.cursor()
#c.execute('''CREATE TABLE webpages(outlinks TEXT, backlinks TEXT, images TEXT)''')

