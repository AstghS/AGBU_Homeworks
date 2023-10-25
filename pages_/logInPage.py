from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.BasePage import BasePage

class LogInPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_user_name_field(self, username):
        # userNameField = self.driver.find_element(By.ID, "ap_email")
        userNameField = self._find_element(By.ID, "ap_email")
        # BasePage.py ից կանչում ենք _fill_fild մեթեթողը, այժմ կարող ենք հաջորդ 2 տեղը հանել դրանք այլևս պետք չեն
        self._fill_field(userNameField, username)
        # userNameField.clear()
        # userNameField.send_keys(username)

    def click_to_continue_Button(self):
        # continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement = self._find_element(By.ID, "continue")
        continueButtonElement.click()

    def fill_password_field(self, password):
        # passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        # BasePage.py ից կանչում ենք _fill_fild մեթեթողը, այժմ կարող ենք հաջորդ 2 տեղը հանել դրանք այլևս պետք չեն
        self._fill_field(passwordFieldElement, password)
        # passwordFieldElement.clear()
        # passwordFieldElement.send_keys(password)
        passwordFieldElement.click()

    def click_to_sign_in_button(self):
        sleep(5)
        # signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        signInButtonElement.click()
        sleep(6)

