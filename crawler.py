import requests as req
#from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = req.get(url)
if response.status_code == 200:
    print("The page was fetched successfully!")
else:
    print("The page could not be fetched.")

