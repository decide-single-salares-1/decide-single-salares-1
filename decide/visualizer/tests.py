from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase
from selenium.webdriver.support.color import Color 


class VisualizerTestCase(BaseTestCase):
    def test_check_funciona_la_pagina(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        
        assert driver.find_element(By.CSS_SELECTOR, ".navbar-brand").text == "Decide, una app para sus votaciones y resultados"


