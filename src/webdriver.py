from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def open_browser(url):
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # browser = webdriver.Firefox(options=options)
    browser = webdriver.Firefox()
    browser.get(url)
    browser.maximize_window()
    # browser.set_window_size(2000, 2000)
    return browser

def clickAmikaOption(browser):
    try:
        # Encontrar o elemento usando o seletor de ID
        click_box = browser.find_element(By.ID, "perg13068")

        # Encontrar todos os elementos radio dentro do elemento clicável
        radios = click_box.find_elements(By.TAG_NAME, "input")

        # Iterar sobre os elementos radio e clicar no que tiver o valor '102974'
        for radio in radios:
            if radio.get_attribute("value") == "102974":
                browser.execute_script("arguments[0].scrollIntoView();", click_box)
                ActionChains(browser).move_to_element(click_box).click(radio).perform()
                break
    except Exception as e:
        print("Erro ao clicar na opção", e)
        return False

def click_submit_button(browser):
    try:
        # Encontrar o elemento usando o seletor de ID
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
