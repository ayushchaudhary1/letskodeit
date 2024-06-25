import time

from selenium.webdriver.common.by import By


class Sydneys:


    page = (By.XPATH, "(//a[@aria-current='page'])[2]")


    def __init__(self, driver):
        self.driver = driver

    def VerifyPageOrder(self):
        time.sleep(5)
        verify = self.driver.find_element(*self.page).is_displayed()
        return verify