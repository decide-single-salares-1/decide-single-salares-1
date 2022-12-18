
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase

class BoothTestCase(BaseTestCase):
    def test_logincheck(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://127.0.0.1:8000/booth/1/")
        driver.set_window_size(1294, 704)
        driver.find_element(By.ID, "username").click()
        driver.find_element(By.ID, "username").send_keys("miggavmar")
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "password").send_keys("migueldecide")
        driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
        elements = driver.find_elements(By.LINK_TEXT, "logout")
        assert len(elements) > 0