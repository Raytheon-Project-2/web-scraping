from bs4 import BeautifulSoup
from helium import *
import time

def scrape():
    # Set URL to scrape from
    url = 'https://sam.gov/content/home'
    driver = start_chrome(url, headless = True) # web driver initialize
    driver.get(url)

    time.sleep(5)

    html=driver.page_source

    # Parse and Save HTML to soup object
    soup = BeautifulSoup(html, "html.parser")

    announcments = soup.find("div", {"class" : "sds-feed"})
    article_links = []
    for a in announcments.find_all('a', href=True):
        article_links.append(a['href'])
    
    for i in article_links:
        if (i.find('article') == -1):
            article_links.remove(i)
    
    for link in article_links:
        print(link)  
    

def main():
    scrape()

if __name__ == '__main__':
    main()

