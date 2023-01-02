import src.webdriver
import sys
import time

def send_request(n: int):
    for username, email in src.generate_fakers.generate_fake_data(n):
        # # time.sleep(5)
        # # src.webdriver.accept_cookies(browser)
        browser = src.webdriver.open_browser('https://psq.mobi:443/$/?psq=1004&c=65')
        time.sleep(5)
        src.webdriver.fill_form_signup(browser, username, email)
        time.sleep(5)
        # src.webdriver.click_submit_button(browser)
        # src.webdriver.close_browser(browser)
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
