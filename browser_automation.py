from bs4 import BeautifulSoup
from helium import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import os
import pandas as pd

def download():
    url = 'https://sam.gov/data-services/Contract%20Opportunities/Archived%20Data?privacy=Public'

    # Changes download directory
    c_options = ChromeOptions()
    prefs = {"download.default_directory" : "C:\\Users\Matthew Choi\OneDrive\Purdue University\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\csvFiles"}
    c_options.add_experimental_option("prefs", prefs)

    #for i in range(1,4): # change 4 to 29
        # Start an instance of chrome
    driver = start_chrome(url, options=c_options) # add headless=True
    driver.get(url)

    #click(S('.usa-button'))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='usa-button'])"))).click()
        # Downloads all of the files present
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='data-service-file-link ng-star-inserted'])"+f'{[1]}'))).click()

        # Check and submit terms of service check boxes
    driver.find_element_by_xpath("//input[@id='term19']").click()
    driver.find_element_by_xpath("//input[@id='term20']").click()
    driver.find_element_by_xpath("//input[@id='term21']").click()
    click(S('.usa-modal-content-submit-btn'))

    time.sleep(5)
    kill_browser()

def db_inject():
    dir_name = "C:\\Users\Matthew Choi\OneDrive\Purdue University\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\csvFiles"
    # establish database connection

    for file in os.listdir(dir_name):
        # if file not in database
        convert_csv_json(file)
            # dump into database
        # else
            # delete file
        NULL

def convert_csv_json(csvFile):
    os.chdir("C:\\Users\Matthew Choi\OneDrive\Purdue University\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\csvFiles")
    df = pd.read_csv(csvFile)
    #add path 
    save_path = "C:\\Users\Matthew Choi\OneDrive\Purdue University\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\jsonFiles"
    file_name = csvFile # change file name
    completeName = os.path.join(save_path, file_name)

    with open(completeName, 'w') as f:
        f.write(df.to_json(orient='records', lines=True))


def main():
    #download()
    db_inject()

    # if running on a clock, periodically clear dir where csv files are downloaded
    
if __name__ == '__main__':
    main()