from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def open_browser(url):
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    with webdriver.Firefox(firefox_profile=firefox_profile) as browser:
        browser.get(url)
        browser.set_window_size(1920, 1080)
        return browser

# def open_browser(url):
#     browser = webdriver.Safari()
#     browser.get(url)
#     return browser

def accept_cookies(browser):
    # Tentar encontrar o botão de "aceitar" ou "fechar" na janela de cookies
    try:
        accept_button = browser.find_element(By.CLASS_NAME, "cookieButton")
        # Mover o cursor do mouse para o elemento antes de clicar nele
        actions = ActionChains(browser)
        actions.move_to_element(accept_button).perform()
        # Clicar no botão
        accept_button.click()
    except:
        print("Erro ao aceitar os cookies")
        return False

def fill_form(browser, username, email):
    user_boxes = browser.find_elements(By.ID, "nome")
    mail_boxes = browser.find_elements(By.ID, "email")
    submit_boxes = browser.find_elements(By.XPATH, "//*[@id='btSubmitProx']")
    if user_boxes:
        user_box = user_boxes[0]
        user_box.send_keys(username)
        print(user_box)
    if mail_boxes:
        mail_box = mail_boxes[0]
        print(mail_box)
        mail_box.send_keys(email)
    if submit_boxes:
        submit_box = submit_boxes[0]
        print(submit_box)
        # Mover o cursor do mouse para o elemento antes de clicar nele
        actions = ActionChains(browser)
        actions.move_to_element(submit_box).perform()
        time.sleep(2)
        submit_box.click()
    return True
