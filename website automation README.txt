Web browser automation README

Browser automation was chosen instead of scraping announcement data because of government restrictions placed on scraping data 
from sam.gov. If this problem occurs again, do not run the code that outputted this problem.

Once run, this code will automatically download contract opporunity data in a csv format from sam.gov. 
One bug that may come up is an outdated chrome driver when using helium. Make sure the driver is always up to date.
Latest versions can be found at https://chromedriver.chromium.org/downloads. For testing purposes, headless mode has
been turned off. When done testing, include the option for headlss browser when starting an instance of chrome.

If there is a need for the file to be kept in a csv format, comment out the convert_csv_json() function as this function
will convert csv files into json files. 