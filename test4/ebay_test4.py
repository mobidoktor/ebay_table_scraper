# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium import webdriver

# # Start the WebDriver and load the page
# wd = webdriver.Firefox()
# wd.get('http://www.ebay.com/itm/New-Radiator-For-Civic-92-00-Del-Sol-93-97-EL-1-5-1-6-L4-Lifetime-Warranty-/201948259311?hash=item2f050de3ef:g:4wgAAOSw4GVYLe8k:sc:ShippingMethodOvernight!33166!US!-1&vxp=mtr')

# # Wait for the dynamically loaded elements to show up
# WebDriverWait(wd, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "tab-content-m"))
#     )

# # And grab the page HTML source
# html_page = wd.page_source
# wd.quit()

# import csv
# import requests

# from BeautifulSoup import BeautifulSoup
# soup = BeautifulSoup(html_page)
# <tbody class="stripe" id="mrc_main_table">
# print soup.prettify()

# 1st Iteration
###################################
# This one should have no errors.
# table = soup.find('table', attrs={'id': 'w1-38ctbl'})
# print table.prettify()
###################################

# 2nd iteration
# Refining search. Working still. 
#####################################
# table = soup.find('table', attrs={'id': 'w1-38ctbl'})
# tbody = table.find('tbody')
# print tbody.prettify()
####################################

# 3rd Iteration targeting rows, stable.
#####################################
# table = soup.find('table', attrs={'id': 'w1-38ctbl'})
# tbody = table.find('tbody')

# for row in tbody.findAll('tr'):
#     print row.prettify()
####################################


# 4th Iteration with fixes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('https://www.ebay.com/itm/322887366109')
        # Insert the URL of the ebay page with a searchable table in the above lin between quotes.
# Wait for the dynamically loaded elements to show up
WebDriverWait(wd, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "tab-content-m"))
    ) 

# And grab the page HTML source
import time
import csv
import requests

from BeautifulSoup import BeautifulSoup

list_of_rows = []
def scraper():
    html_page = wd.page_source
    soup = BeautifulSoup(html_page)
    table = soup.find('table', attrs={'class': 'fTbl'})
    tbody = table.find('tbody')

    for row in tbody.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    wd.find_element_by_xpath('//*[@title="next page"]').click()
    time.sleep(2)

scraper()



outfile = open("./fitment.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
#Data will be exported to a csv file.

wd.quit()
# This just closes the window so it's not annoying.
