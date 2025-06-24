import sqlite3

connection = sqlite3.connect('searchengine.db')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS webpages(url TEXT, images TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS backlinks(source TEXT, backlink TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS outlinks(source TEXT, outlink TEXT)''')
connection.commit()
