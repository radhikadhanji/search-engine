import time 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin

def crawl(url, driver, visited = set()):
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
    next = soup.find('li', class_='next')
    images = soup.find_all('img')
    links = soup.find_all('a', href=True)
    for img in images:
        #get url of all images 
        image_url = urljoin(url, img.get('src'))

    for link in links:
        next_url = link['href']
        #If next url is a wikipedia article and not a subarticle, crawl
        if next_url.startswith('/wiki/') and ':' not in next_url:
            crawl(urljoin(url, next_url), driver, visited)

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Cat'
    webdrive = webdriver.Safari()
    crawl(url, webdrive)
    webdrive.quit()



