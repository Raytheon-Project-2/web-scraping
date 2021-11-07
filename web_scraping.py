from bs4 import BeautifulSoup
from helium import *
import time


def scrape():

    # Set URL to scrape from
    url = 'https://sam.gov/content/home'

    # Initialize Web Driver
    driver = start_chrome(url, headless = True)
    driver.get(url)
    html=driver.page_source

    driver.find_element_by_name('search')
    time.sleep(5)
    soup = BeautifulSoup(html, "html.parser")

    announcements = soup.find("div", {"class" : "sds-feed"})

    # Filtering section
    article_links = []

    # Check article for keyword, if present in text then append
    for a in announcements:
        article_links.append(a['href'])

    # If keyword is not present in link, remove link
    for i in article_links:
        if (i.find('article') == -1):
            article_links.remove(i)
    
    # for link in article_links:
    #     print(link) 
     
    return article_links

def article_content_scrape(links):   
    for link in links:
        print(link)
        sub_driver = start_chrome(link, headless=True)
        sub_driver.get(link)

        time.sleep(5)

        html = sub_driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # Government does not want me scraping their website boo :(
        content = soup.body.text
        content = soup.find("article").find('section', {'class':'ng-binding ng-scope'}).find_all('p')
        print(content)

def main():
    article_links = scrape()
    article_content_scrape(article_links)

if __name__ == '__main__':
    main()
