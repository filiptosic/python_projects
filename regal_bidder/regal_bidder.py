from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import sys
site = #enter regal link as string
username = #enter email as string
password = #enter password as string
bid_price = #enter bid amount as int

options = Options()
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(options=options)
driver.get(site)
time.sleep(1)
search = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[1]/div[4]/div[1]")
search.click()

time.sleep(1)
email = driver.find_element(By.ID, "email")
email.send_keys(username)
time.sleep(1)
next_field = driver.find_element(By.ID, "password")
next_field.send_keys(password)
login_button = driver.find_element(By.XPATH, "//*[@id='account']/div/div/div[2]/button")
login_button.click()

time.sleep(1)
bid_amount = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[1]/div[4]/div[2]/div/form/div[1]/input[1]")
time.sleep(3)
bid_amount.send_keys(bid_price)
time.sleep(5)
# search = driver.find_element(By.ID, "offer-amount-input")
# time.sleep(5)
# search.send_keys("1500")
# # search.send_keys(Keys.RETURN)
# time.sleep(30)