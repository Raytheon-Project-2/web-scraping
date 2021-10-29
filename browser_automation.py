from os import kill
from bs4 import BeautifulSoup
from helium import *
import time

def setup():
    url = 'https://sam.gov/data-services/Contract%20Opportunities/Archived%20Data?privacy=Public'
    # Start an instance of chrome
    driver = start_chrome(url)
    driver.get(url)
    html=driver.page_source
    click(S(".data-service-file-link ng-star-inserted"))

def download():
    NULL

def main():
    setup()

if __name__ == '__main__':
    main()