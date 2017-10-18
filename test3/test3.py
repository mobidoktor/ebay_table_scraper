from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('https://www.ebay.com/itm/Radiator-CU1290-26MM-BETTER-COOLING-PERFORMANCE-for-Honda-Civic-Acura-L4-1-6L-/382228301781?epid=79226765&hash=item58fe9507d5:g:xccAAOSw~oFZvD1o&vxp=mtr')
        # Insert the URL of the ebay page with a searchable table in the above lin between quotes.
# Wait for the dynamically loaded elements to show up
WebDriverWait(wd, 10).until(
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
# def scraper():
table = soup.find('table', attrs={'class': 'fTbl'})
tbody = table.find('tbody')

row = tbody.findAll('tr')

print row

wd.find_element_by_xpath('//*[@title="next page"]').click()
time.sleep(5)

#Run 2
table2 = soup.find('table', attrs={'class': 'fTbl'})
tbody2 = table2.find('tbody')

row2 = tbody2.findAll('tr')

print row2


#     list_of_cells = []
#     for cell in row.findAll('td'):
#         text = cell.text.replace('&nbsp;', '')
#     list_of_cells.append(text)
#     list_of_rows.append(list_of_cells)

# scraper()
# scraper()
# scraper()
# scraper()
# scraper()


# outfile = open("./fitment.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerows(list_of_rows)
# #Data will be exported to a csv file.

# wd.quit()
# # This just closes the window so it's not annoying.
