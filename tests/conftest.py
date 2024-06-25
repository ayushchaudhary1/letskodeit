import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver


@pytest.fixture(scope="module")
def login(driver):
    driver.get("https://ecommercepractice.letskodeit.com/login")

    time.sleep(4)
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
    username.send_keys("ayushvirang123@gmail.com")

    time.sleep(3)
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    password.send_keys("Vinit@123")

    time.sleep(4)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(4)


    yield driver
