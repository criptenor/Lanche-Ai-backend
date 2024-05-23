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

class whatsappWeb:
    def __init__(self, id_loja):
        self.servico=Service(ChromeDriverManager().install())
        self.tempo_maximo_espera=100
        self.iniciarWpp()
        while True:
            self.escutarMensagensPessoas()
        self.driver.quit()

    def iniciarWpp(self, url="https://web.whatsapp.com"):
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

    def escutarMensagensPessoas(self):
        try:
            WebDriverWait(self.driver, 1000000000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak72._ak73")))
            while True:
                divs_mensagem = self.driver.find_elements(By.CSS_SELECTOR, "div._ak72._ak73")
                for div_mensagem in divs_mensagem:
                    # Verificar se a div contém um elemento de mensagem
                    try:

                        num_mensagens = div_mensagem.find_elements(By.CSS_SELECTOR,
                                                               "span.x1rg5ohu.x173ssrc.x1xaadd7.x682dto.x1e01kqd.x12j7j87.x9bpaai.x1pg5gke.x1s688f.xo5v014.x1u28eo4.x2b8uid.x16dsc37.x18ba5f9.x1sbl2l.xy9co9w.x5r174s.x7h3shv[aria-label]")
                    except:
                        break
                    if len(num_mensagens) != 0:
                        # Obter o nome da pessoa
                        nome_elemento = div_mensagem.find_element(By.CSS_SELECTOR, "span.x1rg5ohu._ao3e")
                        nome = nome_elemento.text
                        # Obter a mensagem
                        mensagem_elemento = div_mensagem.find_elements(By.CSS_SELECTOR,
                                                                      "span.x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1rg5ohu._ao3e")
                        try:
                            mensagem = mensagem_elemento[1].text
                        except:
                            mensagem=''

                        # Clicar na mensagem
                        div_mensagem.click()
                        time.sleep(1)  # Aguardar um segundo para carregar o perfil
                        # Verificar se é um perfil de grupo
                        if True:
                            # Clicar no botão de perfil
                            botao_perfil = WebDriverWait(self.driver, self.tempo_maximo_espera).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            'header._amid')))
                            botao_perfil.click()
                            time.sleep(2)
                            try:

                                if 'Grupo' in self.driver.find_element(By.CSS_SELECTOR, 'div.x1jchvi3.x1fcty0u.x40yjcy').text:
                                    continue
                            except:

                                numero_elemento = self.driver.find_element(By.CSS_SELECTOR,
                                                                           "span.x1jchvi3.x1fcty0u.x40yjcy[aria-label]")
                                print(numero_elemento.text)
                                numero_telefone = numero_elemento.text
                                if  'Grupo' in numero_telefone:
                                    print('shii')
                                    actions = ActionChains(self.driver)
                                    actions.send_keys('\ue00c').perform()
                                    botao_perfil = WebDriverWait(self.driver, self.tempo_maximo_espera).until(
                                        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                    'header._amid')))

                                    actions.send_keys('\ue00c').perform()
                                    actions.send_keys('\ue00c').perform()

                                    continue
                                actions = ActionChains(self.driver)
                                actions.send_keys('\ue00c').perform()
                                self.enviar_mensagem('ola, teste, mensagem')
                                actions.send_keys('\ue00c').perform()
                                actions.send_keys('\ue00c').perform()






                # Aguardar um curto período antes de verificar novamente
                time.sleep(1)

        except TimeoutException as e:
            print(e)

    def enviar_mensagem(self, mensagem):
        script = f'''
            async function enviarScript(scriptText){{
                const main = document.querySelector("#main");
                const textarea = main.querySelector(`div[contenteditable="true"]`);

                if(!textarea) throw new Error("Não há uma conversa aberta");

                textarea.focus();
                document.execCommand('insertText', false, scriptText);
                textarea.dispatchEvent(new Event('input', {{bubbles: true}}));
                setTimeout(() => {{
                    (main.querySelector(`[data-testid="send"]`) || main.querySelector(`[data-icon="send"]`)).click();
                }}, 100);

                return 1; // Retorna 1, pois apenas uma mensagem foi enviada.
            }}

            enviarScript(`
            {mensagem}
            `);
        '''
        self.driver.execute_script(script)

    def enviar_mensagem_pelo_js(self, msm):
        actions = ActionChains(self.driver)
        actions.send_keys('\ue00c').perform()
        self.driver.execute_script(f'document.querySelectorAll("").innerHTML="{msm}"')

    def ehPerfilGrupo(self):
        # Verificar se é um perfil de grupo
        try:
            WebDriverWait(self.driver, self.tempo_maximo_espera).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.x1c4vz4f.x2lah0s")))
            return True
        except TimeoutException:
            return False




a=whatsappWeb(1)


