news_scraper.py

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.gazeta.ru/"

#
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class":""})