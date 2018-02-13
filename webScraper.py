from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import time


pageNumber = 10
myCount = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

#loop for each page
for i in range (0,90):

    myPageNumber = str(pageNumber)
    url = "https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=" + myPageNumber + "&bbn=283155&ie=UTF8&qid=1518317950"
    #print(myPageNumber)
    pageNumber = pageNumber + 1
    response = requests.get(url, headers=headers)
    page_html = response.text
    page_soup = soup(page_html, 'html.parser')
    #grabs each listing
    containers = page_soup.findAll("div", {"class":"s-item-container"})
    #print(len(containers))
    print("Current page number: " + myPageNumber)

    for container in containers:
        #print(container)
        #print(myCount)
        myCount = myCount + 1
        #finds book title
        #bookTitle = container.find("a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"}).text
        #print(bookTitle)

        #finds authours name
        #try:
        #    author = container.findAll("a", {"class": "a-link-normal a-text-normal"})
        #    authorName = author[1].text
        #    print(authorName)
        #except IOError:
        #    print("Cannot find author name")
        #else:
        #    author = container.findAll("span", {"class": "a-size-small a-color-secondary"})
        #    authorName = author[1].text
        #    print(authorName)
        ###


        #finds reviews
        #review = container.findAll("a", {"class": "a-size-small a-link-normal a-text-normal"})
        #reviews = review[1].text
        #print(reviews)

        #finds release date
        #releaseDate = container.findAll("span", {"class": "a-size-small a-color-secondary"})
        #release = releaseDate[0].text
        #print(release)
print("Total listings found: " + str(myCount))
