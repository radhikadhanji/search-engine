import sqlite3

connection = sqlite3.connect('searchengine.db')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS webpages(url TEXT, pagetext TEXT, images TEXT, UNIQUE(url, pagetext, images))''')
c.execute('''CREATE TABLE IF NOT EXISTS backlinks(source TEXT, backlink TEXT, UNIQUE(source, backlink))''')
c.execute('''CREATE TABLE IF NOT EXISTS outlinks(source TEXT, outlink TEXT, UNIQUE(source, outlink))''')
connection.commit()
