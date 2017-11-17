from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('https://www.ebay.com/itm/222690454261')
        # Insert the URL of the ebay page with a searchable table in the above lin between quotes.
# Wait for the dynamically loaded elements to show up
WebDriverWait(wd, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "tab-content-m"))
    ) 

# And grab the page HTML source
import time
import csv
import requests

from bs4 import BeautifulSoup  

list_of_rows = []
def scraper():
    html_page = wd.page_source
    soup = BeautifulSoup(html_page, "lxml")
    table = soup.find('table','fTbl')   
    rows = table.find_all('tr')
    next_arrow = wd.find_element_by_xpath('//*[@title="next page"]')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        list_of_rows.append([ele for ele in cols if ele]) # Get rid of empty values
    next_arrow.click()
    time.sleep(2)
scraper()
print list_of_rows



outfile = open("./fitment.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
#Data will be exported to a csv file.

# wd.quit()
# This just closes the window so it's not annoying.