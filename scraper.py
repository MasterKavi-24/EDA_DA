from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import re

from typing import List

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
driver = webdriver.Chrome()

class Item:
    def __init__(self, name: str, rating: float) -> None:
        self.name = name
        self.rating = rating

def amazon(item_name: str):
    driver.get(f"https://www.amazon.com/")
    try:
        captchaCharacters: WebElement = driver.find_element(by=By.ID, value="captchacharacters")
        driver.implicitly_wait(10)
        print("Solve the captcha...")
    except:
        pass

    changeLangPage: WebElement = driver.find_element(by=By.ID, value="icp-nav-flyout")
    changeLangPage.click()
    """ changeLang: WebElement = driver.find_element(by=By.ID, value="a-dropdown-prompt")
    changeLang.click() """

    """ searchBox: WebElement = driver.find_element(by=By.ID, value="twotabsearchtextbox")
    searchBox.send_keys(item_name)
    searchButton: WebElement = driver.find_element(by=By.ID, value="nav-search-submit-button")
    searchButton.click()

    items = driver.find_elements(By.CSS_SELECTOR, "h2 a span")
    for i in items:
        print(i.text) """

    """ ratings = driver.find_element(By.XPATH, "//*[@id=\"a-popover-content-2\"]/div/div/div/div[1]/span")
    # ratings = driver.find_element(By.XPATH, "//span[@data-hook='acr-average-stars-rating-text']")
    for i in ratings:
        print(i.text) """

    """ url: str = driver.current_url
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    for i in doc.find_all('span', attrs={'data-hook': 'acr-average-stars-rating-text'}):
        print(i.text) """


if __name__ == "__main__":
    amazon("jeans pant")
    input("Press enter to quit... ")
