import time 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin
import sqlite3
import json

def crawl(url, driver, connection, c, depth, max_depth, visited = set()):
    if requests.get(url).status_code != 200:
        print("Error: cannot fetch this url")
        return

    if url in visited:
        #return if url is already visited
        return
    visited.add(url)
    print(f'Crawling on {url}')
    #Use safari web driver to handle JS
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #Find all links and crawl the connected pages
    images = soup.find_all('img')
    links = soup.find_all('a', href=True)
    #Get image and outlinks for inputting into the database
    imagelinks = [urljoin(url, img.get('src')) for img in images]
    outlinks = [urljoin(url, link['href']) for link in links if link['href'].startswith('/wiki/') and ':' not in link['href']]
    
    c.execute('''INSERT OR IGNORE INTO webpages VALUES(?,?)''', (url, json.dumps(imagelinks)))
    c.execute('''INSERT OR IGNORE INTO outlinks VALUES(?,?)''', (url, json.dumps(outlinks)))

    #We have to add to backlinks before crawling the next page
    for next in outlinks:
         c.execute('''INSERT OR IGNORE INTO backlinks VALUES(?,?)''', (url, next))
    connection.commit()
    
    if depth < max_depth:
        for next in outlinks:
            crawl(next, driver, connection, c, depth + 1, max_depth, visited)
    else:
        return

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Cat'
    webdrive = webdriver.Safari()
    connection = sqlite3.connect('searchengine.db')
    c = connection.cursor()
    depth = 0
    max_depth = 3
    crawl(url, webdrive, connection, c, depth, max_depth)
    print("Max depth on all links reached. Terminating crawl.")
    connection.close()
    webdrive.quit()



