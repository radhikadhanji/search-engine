import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin

def crawl(url, driver, visited = set()):
    if url in visited:
        #return if url is already visited
        return
    visited.add(url)
    #Use safari web driver to handle JS
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #Find all links and crawl the connected pages
    next = soup.find('li', class_ = 'next')
    if next:
        next_url = next.find('a')['href']
        crawl(urljoin(url, next_url), driver, visited)
    driver.quit()

if __name__ == '__main__':
    url = 'http://quotes.toscrape.com/'
    webdrive = webdriver.Safari()
    crawl(url, webdrive)



