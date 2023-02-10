# There are two types of locators 1) Locators 2) Customized Locators
# Six locators 1) ID 2) Name 3) Linked_text 4) Partial_Linked_Test 5) Class 6) Tag
# Two Customized Locators 1) CSS Selectors 2) XPath
# Four CSS Selectors 1) Tag+ID 2) Tag+Class 3) Tag+Attribute 4) Tag+Class+Attribute
# Two XPath 1) Absolute XPath 2) Relative XPath
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
# service_obj = Service('/home/dell/iqbalFolder/drivers/chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)
# driver.get('https://demo.nopcommerce.com/')

# _________ID, NAME, LINKED_TEXT and PARTIAL_LINKED_TEXT are used to find singal element_________
# Use of ID locators
# driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo IdeaCentre 600 All-in-One PC')
# use of name locators
# driver.find_element(By.NAME, 'q').send_keys('Lenovo IdeaCentre 600 All-in-One PC')
# LINKED TEST AND PARTIAL LINKED TEST
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, 'Register').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Reg').click()

# service_obj = Service('/home/dell/iqbalFolder/drivers/chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)
# driver.get('https://uet.edu.pk/')
# # To find the total numbers of the sliders of the main page using CLASS_NAME selectors
# # if we use find_element, only first element will be selected
# sliders = driver.find_elements(By.CLASS_NAME, 'item')
# print("Total Sliders", len(sliders))
# # to find total number of links on the main page using TAG_NAME selectors
# # if we use find_element, only first element will be selected
# links = driver.find_elements(By.TAG_NAME, 'a')
# print("Total Links:", len(links))
# print("List of Links:", links)


# CSS Selectors
service_obj = Service('/home/dell/iqbalFolder/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://web.facebook.com/')
driver.maximize_window()
# Tag & ID where tag is optional
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, '#email').send_keys('abc@gmail.com')

# Tag & Class where tag is optional
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext._55r1._6luy').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('abs@gmail.com')

# Tag & Attribute where tag is optional
# driver.find_element(By.CSS_SELECTOR, 'input[type=text]').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, '[type=text]').send_keys('abs@gmail.com')

# Tag, class & Attribute where tag is optional
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext._55r1._6luy[type=text]').send_keys('azc@gmail.com')
driver.find_element(By.CSS_SELECTOR, '.inputtext._55r1._6luy[type=text]').send_keys('afc@gmail.com')
# time.sleep(5)