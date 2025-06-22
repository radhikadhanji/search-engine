import requests as req
from bs4 import BeautifulSoup

def crawl(url, visited = set()):
    if url in visited:
        #return if url is already visited
        return
    visited.add(url)
    response = req.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next = soup.find('li', class_ = 'next')
    if next:
        next_url = next.find('a')['href']
        print(next_url)
        crawl(url + next_url, visited)

url = 'http://quotes.toscrape.com'
crawl(url)



