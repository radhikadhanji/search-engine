import time 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sqlite3
import json

def crawl(url, connection, c, depth, max_depth, visited = set()):
    #get response using requests
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        print("Error: cannot fetch this url")
        return

    if url in visited:
        #return if url is already visited
        return
    visited.add(url)
    print(f'Crawling on {url}')
    
    time.sleep(0.5)
    soup = BeautifulSoup(response.text, 'html.parser')
    #Find all links and crawl the connected pages
    images = soup.find_all('img')
    links = soup.find_all('a', href=True)
    #Get page text, image and outlinks for inputting into the database
    pagetext = soup.get_text()
    imagelinks = [urljoin(url, img.get('src')) for img in images]
    outlinks = [urljoin(url, link['href']) for link in links if link['href'].startswith('/wiki/') and ':' not in link['href']]
    
    c.execute('''INSERT OR IGNORE INTO webpages VALUES(?,?,?)''', (url, pagetext, json.dumps(imagelinks)))
    c.execute('''INSERT OR IGNORE INTO outlinks VALUES(?,?)''', (url, json.dumps(outlinks)))

    #We have to add to backlinks before crawling the next page
    for next in outlinks:
         c.execute('''INSERT OR IGNORE INTO backlinks VALUES(?,?)''', (url, next))
    connection.commit()
    
    if depth < max_depth:
        for next in outlinks:
            crawl(next, connection, c, depth + 1, max_depth, visited)
    else:
        return

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Cat'
    connection = sqlite3.connect('searchengine.db')
    c = connection.cursor()
    depth = 0
    max_depth = 3
    crawl(url, connection, c, depth, max_depth)
    print("Max depth on all links reached. Terminating crawl.")
    connection.close()



