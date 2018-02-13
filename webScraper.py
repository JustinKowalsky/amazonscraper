from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import time

url = "https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=10&bbn=283155&ie=UTF8&qid=1518317950"
pageNumber = 10
myCount = 108
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

response = requests.get(url, headers=headers)
page_html = response.text

page_soup = soup(page_html, 'html.parser')

#grabs each listing
containers = page_soup.findAll("div", {"class":"s-item-container"})
container = containers[0]

#finds book title
bookTitle = container.find("a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"}).text
print(bookTitle)

#finds authours name
author = container.findAll("a", {"class": "a-link-normal a-text-normal"})
authorName = author[1].text
print(authorName)

#finds reviews
review = container.findAll("a", {"class": "a-size-small a-link-normal a-text-normal"})
reviews = review[1].text
print(reviews)

#finds release date
releaseDate = container.findAll("span", {"class": "a-size-small a-color-secondary"})
release = releaseDate[0].text
print(release)
