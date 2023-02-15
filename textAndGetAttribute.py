# text() method is used to find the inner
# text of any element
# get_attribute is used to find value of any attribute
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s_obj = Service("C:/Users/iqbal/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
sl = driver.find_element(By.XPATH, " //input[@id='small-searchterms']")
sl.clear()
sl.send_keys('123')
print("Text: ", sl.text)
time.sleep(5)
print("Text: ", sl.get_attribute('placeholder'))
time.sleep(5)