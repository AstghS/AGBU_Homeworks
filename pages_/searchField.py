from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SearchField():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_search_field(self, productName):
       ppp
        searchFieldElement.clear()
        searchFieldElement.send_keys(productName)
        sleep(3)

    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(By.ID, "nav-search-submit-button")
        searchButtonElement.click()
        sleep(5)
