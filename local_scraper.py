from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import os
import re


os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Review:
    def __init__(self):
        self.custName = ""
        self.stars = 0
        self.heading = ""
        self.review = ""
    
    def __repr__(self):
        ...

driver: WebElement = webdriver.Chrome()
url = "file:///C:/Users/srika/Desktop/VIT/6th%20sem/C%20Essentials%20of%20Data%20Analytics/Theory/DA1/Sample%20Review%201.mhtml"

driver.get(url)
totalRatingsStr: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[4]/div").text
rating: str = re.search(r'\d+(\.\d+)?', totalRatingsStr).group()
print(rating)



'''
/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[1]/div/div/div[4]/span/span
/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[2]/div/div/div[4]/span/span
'''

for i in range(1, 11):
    print(driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{i}]/div/div/div[4]/span/span").text)

driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[11]/span/div/ul/li[2]").click()

input("press enter to quit...")