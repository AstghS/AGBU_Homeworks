from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.BasePage import BasePage

class LogInPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def get_element_text(self, text):
        self.get_element_text(text)
        print.(self._find_element(By.XPATH, "//*[@id="nav-xshop"]/a[2])").text)
