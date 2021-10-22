from bs4 import BeautifulSoup
from helium import *
import time

def scrape():

    # Set URL to scrape from
    url = 'https://sam.gov/content/home'

    # Initialize Web Driver
    driver = start_chrome(url, headless = True)
    driver.get(url)

    # Timer for code to run periodically and pull new announcements
    time.sleep(5)
@@ -19,18 +16,15 @@ def scrape():
    soup = BeautifulSoup(html, "html.parser")

    announcements = soup.find("div", {"class" : "sds-feed"})

    # Filtering section
    article_links = []

    # Check article for keyword, if present in text then append
    for a in announcements.find_all('a', href=True):
        article_links.append(a['href'])

    # If keyword is not present in link, remove link
    for i in article_links:
        if (i.find('article') == -1):
            article_links.remove(i)

    # Prints article text
    for link in article_links:
        print(link)

def main():
    scrape()

if __name__ == '__main__':
    main()
