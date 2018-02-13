
from requests import get
from bs4 import BeautifulSoup
import time

pageNumber = 10
myCount = 108
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

#how many pages
for x in range (1,10):

    url = "https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=10&bbn=283155&ie=UTF8&qid=1518317950"
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    print("Page Number: " + str(pageNumber))
    #number of results per page
    amznBooks = soup.find('#result_108')
    print(amznBooks)
    pageNumber = pageNumber + 1





