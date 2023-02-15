# 1) is_displayed (To check whether an element is present or not on the web page)
# 2) is_enabled (Whether element is enabled means can we perform any action on it)
# 3) is_selected (Used for radio buttons and checkbox)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s_obj = Service("C:/Users/iqbal/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
driver.find_element(By.XPATH,  "//a[contains(text(),'Register')]").click()
time.sleep(3)
# is_displayed   # is_enabled
searbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Search Box Disllayed Status:", searbox.is_displayed())
print("Search Box enabled Status:", searbox.is_enabled())
# is_selected
rb_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print("Before selecting, status:", rb_male.is_selected())
rb_male.click()
print("After selecting, status:", rb_male.is_selected())