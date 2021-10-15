from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrape():
    # Set URL to scrape from
    url = 'https://sam.gov/content/home'
    path=r'C:\\Users\\mchoi\\Downloads\\chromedriver_win32\\chromedriver' # chrome driver install path
    driver = webdriver.Chrome(executable_path=path) # web driver initialize
    driver.get(url)

    time.sleep(5)

    html=driver.page_source

    # Parse and Save HTML to soup object
    soup = BeautifulSoup(html, "html.parser")

    announcments = soup.find("div", {"class" : "sds-feed"})
    article_links = announcments.find_all('a')
    print(article_links)

    #append attributes with same class tag and element tag into a list
    #url = []
    #for class_tag in soup.find all("a")  # a could be any class tag
    # e_tag = h2_tag.find('b') # b could be any element tag that inside the class tag
    #url.append(e_tag.attrs['abcd']  #append the the link of the element into url, abcd is the link attribute
    #print(url)
        
def main():
    scrape()

if __name__ == '__main__':
    main()

# use .prettify() to print out nice formatted HTML
