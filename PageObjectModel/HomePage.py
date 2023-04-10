from selenium.webdriver.common.by import By
from selenium import common

class Home:

    def __init__(self, driver):
        self.driver = driver

    button_shop = (By.XPATH,"//a[text()='Shop']")

    def shopItems(self):
     return self.driver.find_element(*Home.button_shop)
    
