from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium package, sub package webdriver, sub package chrome and then service module contains Service class
import time
from selenium.webdriver.common.by import By
s = Service('C:\\Users\iqbal\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://chromedriver.chromium.org/')
time.sleep(5)