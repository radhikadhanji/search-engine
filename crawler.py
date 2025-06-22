import requests as req
import time
import concurrent.futures as futures
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(url, visited = set()):
    if url in visited:
        #return if url is already visited
        return
    visited.add(url)
    #Use safari web driver to handle JS
    driver = webdriver.Safari()
    driver.get(url)
    #delay between requests
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #Find all links and crawl the connected pages
    next = soup.find('li', class_ = 'next')
    if next:
        next_url = next.find('a')['href']
        crawl(url + next_url, visited)
    driver.quit()

urls = ['http://quotes.toscrape.com/js', 'https://www.octoparse.com/blog/how-to-build-a-web-crawler-from-scratch-a-guide-for-beginners']
with futures.ThreadPoolExecutor() as executor:
    executor.map(crawl, urls)



