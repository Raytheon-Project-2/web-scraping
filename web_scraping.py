from bs4 import BeautifulSoup
import requests

def scrape(url):
    source = url
    response = requests.get(source)
    soup = BeautifulSoup(response.text, "lxml")



def main():
    scrape()

if __name__ == '__main__':
    main()
