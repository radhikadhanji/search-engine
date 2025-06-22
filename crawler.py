import time 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin
import sqlite3

def crawl(url, driver, connection, c, visited = set()):
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
    #Add to db (in order: outlinks, backlinks, images)
    c.execute('''INSERT INTO webpages VALUES(?,?,?)''', (links, links, images))
    connection.commit()
    for img in images:
        #get url of all images 
        image_url = urljoin(url, img.get('src'))

    for link in links:
        next_url = link['href']
        #If next url is a wikipedia article and not a subarticle, crawl
        if next_url.startswith('/wiki/') and ':' not in next_url:
            crawl(urljoin(url, next_url), driver, connection, c, visited)

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Cat'
    webdrive = webdriver.Safari()
    connection = sqlite3.connect('searchengine.db')
    c = connection.cursor()
    crawl(url, webdrive, connection, c)
    connection.close()
    webdrive.quit()



