from bs4 import BeautifulSoup
import requests
import time

def scrape(url):
    # Set URL to scrape from
    url = 'https://sam.gov/content/home'
    response = requests.get(url)

    # Parse and Save HTML to soup object
    soup = BeautifulSoup(response.text, "html.parser")

    #append attributes with same class tag and element tag into a list
    #url = []
    #for class_tag in soup.find all("a")  # a could be any class tag
        e_tag = h2_tag.find('b') # b could be any element tag that inside the class tag
        url.append(e_tag.attrs['abcd']  #append the the link of the element into url, abcd is the link attribute
    #print(url)
        
def main():
    scrape("https://sam.gov/content/home")

if __name__ == '__main__':
    main()

# use .prettify() to print out nice formatted HTML
