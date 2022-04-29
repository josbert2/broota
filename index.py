from PIL import Image, ImageDraw, ImageFont
import textwrap
import qrcode

import mysql.connector as mysql

from openpyxl import Workbook
import xlrd
import requests
from io import BytesIO
from random import randrange

import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import InvalidSessionIdException



from time import sleep
import time
from alive_progress import alive_bar, config_handler
from rich import print
from rich.console import Console
import sys
from datetime import date



from selenium.common.exceptions import NoSuchElementException
from sys import platform

def checkElement(el):
    try:
        element = driver.find_element_by_css_selector(el)
        return 1
    except NoSuchElementException:
        return 0

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="broota"
)

URL_BASE = 'https://inversion.broota.com/campanas'
userName = 'joheandroid@gmail.com'
password = 'Hernandez1'
links_url = []

executable_path = "./firefox"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
#driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)
print("Current session is {}".format(driver.session_id))

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
try:
    driver.get(URL_BASE)
except Exception as e:
    print(e.message)


time.sleep(3)

driver.find_element_by_css_selector('.btnlogin').click()
time.sleep(3)
driver.find_element_by_id('email').send_keys(userName)
driver.find_element_by_id('password').send_keys(password)
time.sleep(2)
driver.find_element_by_class_name('btn-success').click()

while checkElement('#btn-mas-campanas'):
    try:
        time.sleep(2)
        driver.find_element_by_css_selector('#btn-mas-campanas').click()
    except Exception as e:
        time.sleep(2)
        
       
links = driver.find_elements_by_css_selector('.ga-caja .card .content-card .btn-ver-proyecto')
for i in range(len(links)):
    links_url.append(links[i].get_attribute('href'))
    cursor = db.cursor()
    cursor.execute("INSERT INTO links (url) VALUES (%s)", (links_url[i],))
    db.commit()
    cursor.close()

