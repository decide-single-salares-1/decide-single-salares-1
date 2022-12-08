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

    def test_check_funcionan_estilos(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        color_h1 = Color.from_string(driver.find_element(By.CSS_SELECTOR, ".heading").value_of_css_property('background-color'))
        
        assert color_h1.rgb == 'rgb(19, 136, 190)'

    def test_check_aparece_boton_funciones_accesibilidad(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        
        assert driver.find_element(By.ID, "boton").text == "Opciones de accesibilidad"

    def test_check_aparecen_opciones_accesibilidad(self):	
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        driver.find_element(By.ID, "boton").click()
        driver.find_element(By.ID, "boton").click()

        assert driver.find_element(By.CSS_SELECTOR, "#acc > h3").text == "Accesibilidad"
       
    
    def test_check_modo_oscuro(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        driver.find_element(By.ID, "boton").click()
        driver.find_element(By.ID, "boton").click()       
        modo_oscuro = Color.from_string(driver.find_element(By.CSS_SELECTOR, "body").value_of_css_property('background'))
        
        assert modo_oscuro.hex == '#ebf2f7'
        
        
