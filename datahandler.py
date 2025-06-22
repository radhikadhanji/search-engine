import sqlite3

connection = sqlite3.connect('searchengine.db')
c = connection.cursor()
#c.execute('''CREATE TABLE webpages(outlinks TEXT, backlinks TEXT, images TEXT)''')

outlinks = 'http://quotes.toscrape.com'
backlinks = 'http://books.toscrape.com/?'
images = ''

#c.execute('''INSERT INTO webpages VALUES(?, ?, ?)''', (outlinks, backlinks, images))
#connection.commit()

c.execute('''SELECT * FROM webpages''')
results = c.fetchall()
print(results)