from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ExtrairAnotaAi:
    def __init__(self):
        self.servico=Service(ChromeDriverManager().install())
        self.tempo_maximo_espera=100
        self.iniciarAnotaAi()
        print(self.extract_image_links_and_names())
        time.sleep(19)


    def iFood(self, url="https://pedido.anota.ai/login/?access_token=eyJhbGciOiJIUzI1NiJ9.eyJpZGNsaWVudCI6IjY1ZWQyYWFkNThhMzIyMDAxMWNjOTNjMiIsImlkcGFnZSI6IjVmMjQ1NjFjMzkyNjZkNzg0NmRhY2JiYyIsImxpbmtfYWNjZXNzZWQiOmZhbHNlLCJ3aGF0c2FwcCI6dHJ1ZX0.tZr_HRlOgJ6CXjCWRdE7fQxdniGv8UTpJ_p1pgaQqu8&from=whats"):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        # Iniciar o navegador
        self.driver = webdriver.Chrome(service=self.servico, options=chromeOptions)
        self.driver.get(url)

    def extract_image_links_and_names(self):
        # Esperar até que o elemento de categoria-grid apareça
        WebDriverWait(self.driver, self.tempo_maximo_espera).until(EC.presence_of_element_located((By.CLASS_NAME, "category-grid")))

        # Encontrar todos os elementos div dentro do elemento com a classe "category-grid"
        div_elements = self.driver.find_elements(By.CSS_SELECTOR, ".category-grid")

        image_links_and_names = []
        nomes=[]

        # Iterar sobre os elementos div encontrados
        for div_element in div_elements:
            try:
                # Encontrar o elemento de imagem dentro do div
                image_element = div_element.find_element(By.CSS_SELECTOR, "img.category-image")
            except:
                continue
            if image_element.get_attribute("alt") in nomes:
                continue
            # Extrair o link da imagem e o atributo 'alt' como o nome
            image_link = image_element.get_attribute("src")
            image_name = image_element.get_attribute("alt")
            image_element.click()
            WebDriverWait(self.driver, self.tempo_maximo_espera).until(
                EC.presence_of_element_located((By.CLASS_NAME, "items")))
            url=self.driver.current_url
            self.driver.back()
            WebDriverWait(self.driver, self.tempo_maximo_espera).until(
                EC.presence_of_element_located((By.CLASS_NAME, "category-grid")))
            # Adicionar o link da imagem e o nome à lista
            image_links_and_names.append({"name": image_name, "link": image_link, "url": url})

        return image_links_and_names

anotaai=ExtrairAnotaAi()
