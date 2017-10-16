from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('http://www.ebay.com/itm/1290-Fits-Honda-Civic-Del-Sol-Radiator-92-98-1-5-1-6-Acura-EL-01-1-7-L4-/201438758818?hash=item2ee6af87a2:g:EQEAAOSw7FRWYZ2d&vxp=mtr')

# Wait for the dynamically loaded elements to show up
WebDriverWait(wd, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "tab-content-m"))
    )

# And grab the page HTML source
html_page = wd.page_source

import csv
import requests

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html_page)

table = soup.find('table', attrs={'class': 'fTbl'})
tbody = table.find('tbody')

list_of_rows = []
for row in tbody.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

wd.find_element_by_xpath('//*[@title="next page"]').click()


outfile = open("./ebay.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)


# wd.quit()