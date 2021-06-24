from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd
  
# create webdriver object
driver = webdriver.Chrome()

# read file
data = pd.read_csv("stocks.csv")

prices = []

print("!======Getting data======!")
# get data from google finance
for name in data["Symbol"]:
	driver.get("https://www.google.com/finance/")
	time.sleep(0.5)
	input_field = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]')
	input_field.send_keys(name)
	input_field.send_keys(Keys.ENTER)
	time.sleep(2)
	price = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[3]/main/div[2]/c-wiz/div/div[1]/div/div[1]/div[1]/div/div[1]/div/span/div/div')
	prices.append(price.text)

print("!======Writing data======!")
data["prices"] = prices
data.to_csv('stocks.csv', header=True, index=False)
print("!======Done======!")
