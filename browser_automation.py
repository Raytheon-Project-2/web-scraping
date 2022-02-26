from helium import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import os
import pandas as pd
import pymongo
import json

# change username in path when switching laptop to desktop
# make sure chrome driver is up to date

def download():
    url = 'https://sam.gov/data-services/Contract%20Opportunities/Archived%20Data?privacy=Public'

    # Changes download directory
    c_options = ChromeOptions()
    prefs = {"download.default_directory" : "C:\\Users\Matthew Choi\OneDrive\Purdue University\Junior year (2021-2022)\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\csvFiles"}
    c_options.add_experimental_option("prefs", prefs)

    for i in range(1,30): # number of files
        # Start an instance of chrome
        driver = start_chrome(url, options=c_options, headless=False) # add headless=True
        driver.get(url)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='usa-button'])"))).click()
        # Downloads all of the files present
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='data-service-file-link ng-star-inserted'])"+f'{[i]}'))).click()
    
        # Check and submit terms of service check boxes
        driver.find_element_by_xpath("//input[@id='term19']").click()
        driver.find_element_by_xpath("//input[@id='term20']").click()
        driver.find_element_by_xpath("//input[@id='term21']").click()
        click(S('.usa-modal-content-submit-btn'))

        time.sleep(5) # need fast wifi speed
        kill_browser()

def quality_check(df):
    # data cleansing
    if(df['Description'].isnull().values.any()):
        df.dropna()
    
    # extract only necessary columns in df, change if need be
    df = df.loc[:,['NoticeId', 'Title', 'Department/Ind.Agency', 'Description','PostedDate', 'ArchiveDate', 'ZipCode','AwardDate','Award$']]
    print(df)

    return df


def db_inject():
    dir_name = "C:\\Users\Matthew Choi\OneDrive\Purdue University\Junior year (2021-2022)\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\csvFiles"
    
    # establish database connection
    myclient = pymongo.MongoClient("mongodb://128.211.160.177:20201/")
    mydb = myclient["NLP-Testing"]
    mycol = mydb["Contract Opportunities"]

    for file in os.listdir(dir_name):
        convert_csv_json(file)

    # Check this code
    os.chdir("C:\\Users\Matthew Choi\OneDrive\Purdue University\Junior year (2021-2022)\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\jsonFiles")
    for i in os.listdir():
        with open(i) as f:
            file_data = json.load(f)
        mycol.insert_many(file_data)


def convert_csv_json(csvFile):
    # change directory
    os.chdir("C:\\Users\Matthew Choi\OneDrive\Purdue University\Junior year (2021-2022)\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\csvFiles")
    df = pd.read_csv(csvFile,encoding="ISO-8859-1")
    
    df = quality_check(df)

    save_path = "C:\\Users\Matthew Choi\OneDrive\Purdue University\Junior year (2021-2022)\Fall 2021\DMCP Raytheon BI\BI_project_repo\web scraping\web-scraping\jsonFiles"
    file_name = csvFile
    completeName = os.path.join(save_path, file_name)

    # write csv to json
    with open(completeName, 'w') as f:
        f.write(df.to_json(orient='records', lines=True))
    

def main():
    download()
    db_inject()

    # if running on a clock, periodically clear dir where csv files are downloaded
    
if __name__ == '__main__':
    main()
