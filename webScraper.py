from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import time


pageNumber = 10
myCount = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
csvHeaders = "Book Title, Author's Name, #Reviews, Release Date \n"

f = open("authors.csv", "w", encoding="utf-8")
f.write(csvHeaders)
f.write("\n")
#loop for each page
for i in range (0,100):

    myPageNumber = str(pageNumber)
    if pageNumber > 100:
        break
    url = "https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=" + myPageNumber + "&bbn=283155&ie=UTF8&qid=1518317950"
    pageNumber = pageNumber + 1
    response = requests.get(url, headers=headers)
    page_html = response.text
    page_soup = soup(page_html, 'html.parser')
    #grabs each listing
    containers = page_soup.findAll("div", {"class":"s-item-container"})
    print("Working. Please wait....")

    for container in containers:

        #finds reviews
        review = container.find("div", {"class": "a-column a-span5 a-span-last"})
        if (review) == None:
            continue
        reviews = review.find("a", {"class": "a-size-small a-link-normal a-text-normal"})
        if (reviews) == None:
            continue
        reviews = reviews.text
        if (reviews) == "See Details":
            continue
        myReviews = reviews.replace(',', '')
        if (reviews).isdigit() == False:
            continue
        myNewReviews = int(myReviews)
        if myNewReviews >= 25:
            continue

        #finds book title
        bookTitle = container.find("a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
        myBookTitle = bookTitle.text
        if (bookTitle) == None:
            continue
        bookTitle = bookTitle.text
        #f.write(str(bookTitle) + "\n")

        #finds authours name
        author = container.find("div", {"class": "a-row a-spacing-none"})
        authorName = container.find("span", {"class": "a-size-small a-color-secondary"})
        authorName = authorName.findNext("span", {"class": "a-size-small a-color-secondary"})
        authorName = authorName.findNext("span", {"class": "a-size-small a-color-secondary"}).text
        #f.write(authorName + "\n")


        #f.write(str(myReviews) + "\n")

        #finds release date
        releaseDate = container.find("span", {"class": "a-size-small a-color-secondary"})
        releaseDate = container.findNext("span", {"class": "a-size-small a-color-secondary"})
        release = releaseDate.text
        #f.write(str(release) + "\n")
        #f.write("\n")

        newBookTitle = bookTitle.replace(",", "")
        newAuthorName = authorName.replace(",", "")
        newRelease = release.replace(",", "")
        f.write(newBookTitle + "," + newAuthorName + "," + myReviews + "," + newRelease + "\n")
        myCount = myCount + 1

        #end of for loop
print(myPageNumber)
f.write("\n")
f.write("Total listings found: " + str(myCount))
print("Total listings found: " + str(myCount))
f.close()

