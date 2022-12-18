from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase
from selenium.webdriver.support.color import Color 
import os


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
        
        
    def test_check_modo_alto_contraste(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        driver.find_element(By.ID, "boton").click()
        driver.find_element(By.ID, "boton").click()
        driver.find_element(By.ID, "switch3").click()
        color_tabla= Color.from_string(driver.find_element(By.CSS_SELECTOR, "thead th:nth-child(1)").value_of_css_property('color'))
        
        assert color_tabla.rgba == 'rgba(0, 0, 0, 1)'   
    
    def test_creacion_de_graficas_lineas(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        #le damos la ruta de la imagen que se crea con las barras por lo que si existe es que se crean las barras
        ruta_imagen = "barras_simple.png"
        
        # Comprueba si la imagen existe en la carpeta especificada tras visitar el visualizer
        assert os.path.exists(ruta_imagen)

    def test_creacion_de_graficas_pastel(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        #le damos la ruta de la imagen que se crea con las barras por lo que si existe es que se crean las barras
        ruta_imagen = "pie_simple.png"
        
        # Comprueba si la imagen existe en la carpeta especificada tras visitar el visualizer
        assert os.path.exists(ruta_imagen)
        
    def test_creacion_de_PDF(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://localhost:8000/visualizer/1/")
        #le damos la ruta de la pdf que se crea con las barras por lo que si existe es que se crean las barras
        ruta_pdf = "barras.pdf"
        
        # Comprueba si la pdf existe en la carpeta especificada tras visitar el visualizer
        assert os.path.exists(ruta_pdf)
        

  
 
 