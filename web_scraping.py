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
    article_links = [] # list of article links in announcements

    for a in announcments.find_all('a', href=True):
        article_links.append(a['href'])
    
    print(article_links)

        
def main():
    scrape()

if __name__ == '__main__':
    main()

# use .prettify() to print out nice formatted HTML
