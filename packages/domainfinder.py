import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

domailNotFoundCount = 0
fname = []
lname = []
desig = []
cname = []
location = []
domain_list = []


def LinkedinDomainfinder(request, driver):
    reader = csv.DictReader(open("D://Exponential-X//fordomain.csv"))
    for raw in reader:
        company_name = raw['Company Name']
        print(company_name)
        driver.get(
            'https://www.linkedin.com/search/results/companies/?origin=DISCOVER_FROM_SEARCH_HOME')
        wait = WebDriverWait(driver, 10)
        inpt = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @aria-label='Search']"))
        )
        inpt.clear()
        inpt.send_keys(company_name, Keys.ENTER)
        time.sleep(2)
        try:
            dom = driver.find_element_by_link_text(company_name)
            driver.implicitly_wait(5)
        except:
            print("Domain of ", company_name, "is Not Found..")
            domailNotFoundCount = domailNotFoundCount + 1
            continue
        dom.click()
        time.sleep(2)
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        driver.implicitly_wait(10)
        div_section = soup.find(
            'div', {'class': 'org-top-card-primary-actions__inner'})

        fname.append(raw['First Name'])
        lname.append(raw['Last Name'])
        desig.append(raw['Designation'])
        cname.append(raw['Company Name'])
        location.append(raw['Location'])

        for a in div_section.find_all('a', href=True):
            dom = a['href'].split("//")
            if 'www' in dom[1]:
                d = dom[1].split("/")[0][4:]
                print(d)
                domain_list.append(d)
    #             cur.execute("insert into domain_table(FirstName,LastName,Designation,CompanyName,Location,Domain) values(%s,%s,%s,%s,%s,%s)",(raw['First Name'],raw['Last Name'],raw['Designation'],raw['Company Name'],raw['Location'],str(d)))
            else:
                d = dom[1].split("/")[0]
                print(d)
                domain_list.append(d)
    #             cur.execute("insert into domain_table(FirstName,LastName,Designation,CompanyName,Location,Domain) values(%s,%s,%s,%s,%s,%s)",(raw['First Name'],raw['Last Name'],raw['Designation'],raw['Company Name'],raw['Location'],str(d)))
    #         con.commit()
        time.sleep(1)
    # con.close()
    print(domain_list)
