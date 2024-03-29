from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup
# import requests
import re
from typing import List

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# driver: webdriver = webdriver.Chrome()
driver: WebElement = webdriver.Chrome()

class Item:
    def __init__(self, name: str, rating: float) -> None:
        self.name = name
        self.rating = rating
        self.reviews = []

def amazon(item_name: str):
    urls: List[str] = []
    driver.get(f"https://www.amazon.in/")
    try:
        captchaCharacters: WebElement = driver.find_element(by=By.ID, value="captchacharacters")
        driver.implicitly_wait(10)
        print("Solve the captcha...")
    except:
        pass

    driver.get("https://www.amazon.in/customer-preferences/country")
    selectCountry: Select = Select(driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/span/select"))
    selectCountry.select_by_visible_text("India")
    selectIndia: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/ul/li[9]/a")
    selectIndia.click()
    backToWebsiteButton: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[2]/div[3]/div[3]/span")

    original_window = driver.current_window_handle
    backToWebsiteButton.click()
    # Wait for the new tab to appear (adjust timeout as needed)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    all_windows = driver.window_handles
    new_window = [window for window in all_windows if window != original_window][0]
    # Switch focus to the new tab
    driver.switch_to.window(new_window)
    # Close the new tab
    driver.close()
    # Switch back to the original tab (optional)
    driver.switch_to.window(original_window)

    '''
    from selenium.webdriver.common.keys import Keys
    button.click()
    # Simulate pressing Ctrl+W (or Command+W on Mac) to close the new tab
    # **Note:** This approach might not work consistently across browsers.
    actions = webdriver.ActionChains(driver)
    actions.send_keys(Keys.CONTROL + "w").perform()
    '''

    driver.get(f"https://www.amazon.in/s?k={'+'.join(item_name.split(' '))}&s=review-rank")

    urls = []

    i = 2
    # i goes to 52 for "kurta shirt"
    regex_pattern = r'(https://www\.amazon\.in/.+/dp/\w+/)'
    while True:
        if (i == 15): break
        xpath = f"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{i}]"
        try:
            element = driver.find_element(by=By.XPATH, value=xpath)
            
            if 'data-asin' in element.get_attribute('outerHTML'):
                data_asin_value = element.get_attribute('data-asin')
                
                # Check conditions for 'data-asin' value
                if data_asin_value.isalnum() and data_asin_value.isupper() and len(data_asin_value)==10:
                    # print(f"Valid data-asin value: {data_asin_value}")
                    # print(element.find_element(by=By.TAG_NAME, value="a").get_attribute("href"))

                    link = element.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
                    match = re.search(regex_pattern, link)
                    short_link = match.group(1)
                    urls.append(short_link)

                else:
                    # print(f"Invalid data-asin value: {data_asin_value}")
                    pass
            
            i += 1
        # except NoSuchElementException:
        except:
            print("no such elem")
            break
    
    print(urls)
    

    """ searchBox: WebElement = driver.find_element(by=By.ID, value="twotabsearchtextbox")
    searchBox.send_keys(item_name)
    searchButton: WebElement = driver.find_element(by=By.ID, value="nav-search-submit-button")
    searchButton.click()

    # sort_by: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/span[2]/div/h1/div/div[4]/div/div/form/span/span/span/span")
    # sort_by.click()
    # avg_cust_review: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[8]/div/div/ul/li[4]/a")
    # avg_cust_review.click()
    sort_by: Select = Select(driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/span[2]/div/h1/div/div[4]/div/div/form/span/span/span/span"))
    sort_by.select_by_visible_text("Avg. Customer Review")

    # /html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]
    # /html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]
    # /html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[52]


    # items = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div")
    # for i in items:
    #     for j in i.find_elements(by=By.TAG_NAME, value='a'):
    #         urls.append(j.get_attribute("href"))
    # print(urls, len(urls)) """

    items: List[Item]

    for i in range(2):
        reviewUrl: str = urls[i].replace("dp", "product-reviews")
        driver.get(reviewUrl)

        reviews_count: str = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[4]/div").text
        reviews_count = re.search(r'(\d+)\s+with\s+reviews', reviews_count).group(1)
        print("ratings with review:", reviews_count, int(reviews_count)/10)


        print("wts dis:", driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/h1/a").text)
        

        totalRatingsStr: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/span").text
        # rating: re.Match = re.search(r'\d+(\.\d+)?', totalRatingsStr).group(0)
        print("totalRatingsStr:", totalRatingsStr)

        for j in range(1, 11):
            try:
                print(f"rating {j}:", driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{j}]/div/div/div[4]/span/span").text)
            except:
                # less than 10 comments in that page, skip
                pass
        
        # go to next page
        # cur page: https://www.amazon.in/KINGDOM-WHITE-Cloudie-Sleeves-Regular/product-reviews/B0BGQG2T54/
        # nxt page: https://www.amazon.in/KINGDOM-WHITE-Cloudie-Sleeves-Regular/product-reviews/B0BGQG2T54/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber=2
        # actually nvm, just go by click :(
        
        # nextPage: WebElement = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[11]/span/div/ul/li[2]/a")
        # nextPage.click()

        """ for i in urls:
            driver.get(i) """


if __name__ == "__main__":
    amazon("kurta shirt")
    input("Press enter to quit... ")
