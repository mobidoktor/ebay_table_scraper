from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('http://www.ebay.com/itm/1290-New-Aluminum-Radiator-for-1992-2000-Honda-Civic-1997-00-Acura-EL-L4-1-6L-/232270236265?hash=item3614628a69:g:buUAAOSwOddYx0qA&vxp=mtr')

# Wait for the dynamically loaded elements to show up
WebDriverWait(wd, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "tab-content-m"))
    )

# And grab the page HTML source
html_page = wd.page_source
import time
import csv
import requests

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html_page)

list_of_rows = []
def scraper():
    table = soup.find('table', attrs={'class': 'fTbl'})
    tbody = table.find('tbody')

    for row in tbody.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    wd.find_element_by_xpath('//*[@title="next page"]').click()
    time.sleep(5)

scraper()
scraper()
scraper()
scraper()
scraper()


outfile = open("./ebay.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)


# wd.quit()