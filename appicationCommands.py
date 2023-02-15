# Three types of application commands
# 1) Title 2) Current Url  3) Page source
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s_obj = Service("C:/Users/iqbal/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get('https://www.orangehrm.com/')
print(driver.title)    # will print the title of the current page
print(driver.current_url)  # will print the current url of the current pape
# print(driver.page_source)  # will print source code of the current page
