#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#extract information from each job posting and append it to a list 

from bs4 import BeautifulSoup
from helium import *
import time 
from datetime import date

def scrape1():
    url = 'https://www.usajobs.gov/?c=opportunities'
    driver = start_chrome(url, headless = True)
    driver.get(url)
                   
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    hrefs_list = []
    jobs_list = []
    scrape_list = []
    
# get all hraf link for each job category
    for link in soup.find_all("a",{"class": "usajobs-landing-find-opportunities__job"}):
        hrefs_list.append(link['href'])
#open each category link in new browser
    for term in hrefs_list:
        new_url = 'https://www.usajobs.gov'+ term
        driver = start_chrome(new_url, headless = True)
        driver.get(new_url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
#scrape each link for all job box        
        job_link = soup.find_all("a",{'class':'usajobs-search-result--card__body'})
        
#scrape each box for text information about the job (department, agency, and summary) and append to scrape list              
        for job in job_link:
        
            data = [item.get("data-document-id") for item in soup.find_all("a")]
            
            dataID = list(filter(None, data))
            
            scrape_list.append((dataID))
        
    print(scrape_list)      

scrape1()

