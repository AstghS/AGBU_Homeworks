from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class CartPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def clck_to_cart_button(self):
        cartButtonElement = self.driver.find_element(By.ID, "nav-cart-count")
        cartButtonElement.click()

    def delete_first_item_from_cart(self):
        deleteButtonElement = self.driver.find_element(By.NAME, "submit.delete.b4fc750f-0dda-46d2-bd47-4eded5c03870")
        deleteButtonElement.click()
        sleep(5)