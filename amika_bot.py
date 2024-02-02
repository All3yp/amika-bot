import src.webdriver
import sys
import time
import random

# Dicionário com os valores do HTML
options_dict = {
    '109558': 'Amika Coffeehouse',
    '109559': 'Le Pain Le Café',
    '109560': 'Atelier 1913',
    '109561': 'Tipo Café',
    '109562': 'Torra Café'
}

def random_time():
    return 2 #random.uniform(1, 10)

def send_request(n: int):
    for username, email in src.generate_fakers.generate_fake_data(n):
        browser = src.webdriver.open_browser('https://psq.mobi/$/main.asp?psq=1065&c=65&q=1')
        time.sleep(random_time())
        src.webdriver.fill_form_signup(browser, username, email)
        time.sleep(random_time())
        src.webdriver.clickAmikaOption(browser, options_dict)
        time.sleep(random_time())
        src.webdriver.click_submit_button(browser)
        time.sleep(random_time())
        browser.close()
    return True

# MARK: - Main
if __name__ == '__main__':
    n = int(sys.argv[1])
    
    # Enviar a solicitação e verificar se foi bem-sucedida
    success = send_request(n)
    if success:
        print("Solicitação enviada com sucesso")
    else:
        print("Erro ao enviar a solicitação")
