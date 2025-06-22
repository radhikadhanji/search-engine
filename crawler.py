import time
from concurrent.futures import ProcessPoolExecutor
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
        print(next_url)
        crawl(url + next_url, visited)
    driver.quit()

if __name__ == '__main__':
    urls = ['http://quotes.toscrape.com/js', 'https://www.octoparse.com/blog/how-to-build-a-web-crawler-from-scratch-a-guide-for-beginners']
    with ProcessPoolExecutor() as executor:
        #Multithreading with ProcessPoolExecutor
        executor.map(crawl, urls)



