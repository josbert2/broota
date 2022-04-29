from os import link
from tabnanny import check
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
data = []
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

cursor = db.cursor()
cursor.execute('SELECT link FROM inversionistas')
result_set = list(cursor.fetchall())
cursor.close()

for j in result_set:
    links_url.append(j[0])



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
time.sleep(5)

for i in range(len(links_url)):
    print('links: ' + str(i) + ' de ' + str(len(links_url)))
    driver.get(links_url[i])
    time.sleep(1)
    driver.implicitly_wait(0.5)
    time.sleep(2)
    if checkElement('.btn-linkedin'):
        linkedin = driver.find_element_by_css_selector('.btn-linkedin').get_attribute('href')
    else:
        linkedin = 0  
    print(links_url[i])
    inversionistas = driver.find_elements_by_css_selector('.card-campana.z-depth-1')
    nombre = driver.find_element_by_css_selector('.offset-md-1.col-md-6.info-publico h2').text
    campañas = []
    time.sleep(1)
    for j in inversionistas:
        if checkElement('.col-md-10.right h4'):
            campañas.append(j.find_element_by_css_selector('.col-md-10.right  h4').text)
        else:
            campañas.append(0)
    if checkElement('.card-campana.z-depth-1'):
        campañas = ','.join(campañas)
    else:
        campañas = 0
    cursor = db.cursor()
    cursor.execute("INSERT INTO campañas_invertidas (nombre, campañas_invertidas, links_campañas, linkedin ) VALUES (%s, %s, %s, %s)", (str(nombre), str(campañas), str(links_url[i]), str(linkedin)))
    db.commit()
    cursor.close()
  
  
        
   
    


