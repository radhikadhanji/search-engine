import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(url, driver, visited = set()):
    if url in visited:
        #return if url is already visited
        return
    visited.add(url)
    #Use safari web driver to detect JS
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    next = soup.find('li', class_ = 'next')
    if next:
        next_url = next.find('a')['href']
        print(next_url)
        crawl(url + next_url, driver, visited)

url = 'http://quotes.toscrape.com/js'
driver = webdriver.Safari()
crawl(url, driver)
driver.quit()



