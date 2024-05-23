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

class ExtrairIfood:
    def __init__(self):
        self.servico=Service(ChromeDriverManager().install())
        self.tempo_maximo_espera=100
        self.iniciarIfood()
        print(self.extrairProdutos())
        time.sleep(19)


    def iniciarIfood(self, url="https://www.ifood.com.br/delivery/rio-de-janeiro-rj/pizza-time-vila-da-penha-vila-da-penha/e06d85d3-75f0-4308-a813-3f7095e9dbbe"):
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

    def extrairProdutos(self):
        # Inicializa o driver do Selenium (certifique-se de ter o ChromeDriver ou outro driver instalado)


        if True:

            self.driver.execute_script("window.scrollBy(0, 3000);")
            time.sleep(2)

            menu_categories=WebDriverWait(self.driver, 45).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "restaurant-menu-group")))
            # Encontra todas as categorias de menu

            result = []

            # Itera sobre as categorias de menu
            for category in menu_categories:
                category_name = category.find_element(By.TAG_NAME, "h2")
                print("Categoria:", category_name.text)

                # Encontra todos os itens de menu dentro da categoria atual
                menu_items = category.find_elements(By.TAG_NAME, 'li')

                # Itera sobre os itens de menu
                for item in menu_items:
                    product_name = item.find_element(By.CLASS_NAME, 'dish-card__description').text
                    product_link = item.find_element(By.CLASS_NAME, 'dish-card').get_attribute('href')
                    print("   Nome do Produto:", product_name)
                    print("   Link do Produto:", product_link)

                    # Adiciona as informações ao resultado
                    result.append(
                        {"category": category_name, "product_name": product_name, "product_link": product_link})

            return result






anotaai=ExtrairIfood()

