from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def open_browser(url, headless):
    options = webdriver.FirefoxOptions()
    if headless: 
        options.add_argument("--headless")
    browser = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    browser.get(url)
    browser.maximize_window()
    return browser

# Função para obter o texto do elemento clicado usando o dicionário
def get_clicked_option_text(value, options_dict):
    if value in options_dict:
        return options_dict[value]
    else:
        return "Opção não encontrada no dicionário"

# Função com a chamada para obter o texto do elemento clicado
def clickAmikaOption(browser, options_dict):
    try:
        click_box = browser.find_element(By.ID, "perg13935")

        # Encontrar todos os elementos radio dentro do elemento clicável
        radios = click_box.find_elements(By.TAG_NAME, "input")

        # Iterar sobre os elementos radio e clicar no que tiver o valor '109558'
        for radio in radios:
            if radio.get_attribute("value") == "109558":
                browser.execute_script("arguments[0].scrollIntoView();", click_box)
                ActionChains(browser).move_to_element(click_box).click(radio).perform()

                if radio.is_selected():
                    option_text = get_clicked_option_text(radio.get_attribute("value"), options_dict)
                    print(f"\n{'='*30}\nOpção: '{option_text}' clicada com sucesso.\n{'='*30}\n")

                else:
                    print("Erro: A opção não foi clicada corretamente.")
                break
    except Exception as e:
        print("Erro:", e.with_traceback)
        return False

def click_submit_button(browser):
    try:
        submit_box = browser.find_element(By.ID, "btSubmitEnviar")

        # Mover o cursor do mouse para o elemento antes de clicar nele
        browser.execute_script("arguments[0].scrollIntoView();", submit_box)
        actions = ActionChains(browser)
        actions.move_to_element(submit_box).perform()
        submit_box.click()
    except:
        print("Erro ao clicar no botão de envio")
        return False

def fill_form_signup(browser, username, email):
    user_boxes = browser.find_elements(By.ID, "nome")
    mail_boxes = browser.find_elements(By.ID, "email")
    submit_boxes = browser.find_elements(By.XPATH, "//*[@id='btSubmitProx']")
    if user_boxes:
        user_box = user_boxes[0]
        user_box.send_keys(username)
    if mail_boxes:
        mail_box = mail_boxes[0]
        mail_box.send_keys(email)
    if submit_boxes:
        submit_box = submit_boxes[0]
        # Mover o cursor do mouse para o elemento antes de clicar nele
        actions = ActionChains(browser)
        actions.move_to_element(submit_box).perform()
        time.sleep(2)
        submit_box.click()
    return True
