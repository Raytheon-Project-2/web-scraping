from bs4 import BeautifulSoup
import requests

def scrape(url):
    source = url
    response = requests.get(source)
    soup = BeautifulSoup(response.text, "lxml")

    #append attributes with same class tag and element tag into a list
    #url = []
    #for class_tag in soup.find all("a")  # a could be any class tag
        e_tag = h2_tag.find('b') # b could be any element tag that inside the class tag
        url.append(e_tag.attrs['abcd']  #append the the link of the element into url, abcd is the link attribute
    #print(url)
        
def main():
    scrape()

if __name__ == '__main__':
    main()

# use .prettify() to print out nice formatted HTML