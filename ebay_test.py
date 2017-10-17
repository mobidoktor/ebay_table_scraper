from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('http://www.ebay.com/itm/New-Radiator-For-Civic-92-00-Del-Sol-93-97-EL-1-5-1-6-L4-Lifetime-Warranty/201948259311?_trkparms=aid%3D555018%26algo%3DPL.SIM%26ao%3D2%26asc%3D41375%26meid%3D23143fef5bd549569d352b71285a9c06%26pid%3D100005%26rk%3D1%26rkt%3D6%26sd%3D201438758818&_trksid=p2047675.c100005.m1851')

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


outfile = open("./ebay.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)


# wd.quit()