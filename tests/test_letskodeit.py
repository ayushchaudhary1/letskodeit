import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from pages.Sydney import Sydneys


def test_dashboard_access(login):
    driver = login
    time.sleep(6)
    header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//a[@aria-current='page'])[2]")))
    assert header.is_displayed()

def test_verifypageorder(driver):
    sd = Sydneys(driver)
    assert sd.VerifyPageOrder() == True, "Not shown"