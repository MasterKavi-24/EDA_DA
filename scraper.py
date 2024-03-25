from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import requests
# import re
from typing import List

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
driver = webdriver.Chrome()

class Item:
    def __init__(self, name: str, rating: float) -> None:
        self.name = name
        self.rating = rating

def amazon(item_name: str):
    driver.get(f"https://www.amazon.in/")
    try:
        captchaCharacters: WebElement = driver.find_element(by=By.ID, value="captchacharacters")
        driver.implicitly_wait(10)
        print("Solve the captcha...")
    except:
        pass
    searchBox: WebElement = driver.find_element(by=By.ID, value="twotabsearchtextbox")
    searchBox.send_keys(item_name)
    searchButton: WebElement = driver.find_element(by=By.ID, value="nav-search-submit-button")
    searchButton.click()

    items = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]")
    for i in items:
        print(i.find_element(by=By.XPATH, value='/div/div/div/div/span/div/div/div[1]/div/span/a').text)



if __name__ == "__main__":
    amazon("kurta shirt")
    input("Press enter to quit... ")
