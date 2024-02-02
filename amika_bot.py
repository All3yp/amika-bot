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
    return random.uniform(1, 10)

def send_request(n: int, headless: bool = False):
    count = 0
    start = time.time()
    for username, email in src.generate_fakers.generate_fake_data(n):
        print("\n","="*50, sep="")
        count+=1
        print(f"{count} ~ Gerando nome de usuário e email")
        browser = src.webdriver.open_browser('https://psq.mobi/$/main.asp?psq=1065&c=65&q=1', headless)
        time.sleep(random_time())
        src.webdriver.fill_form_signup(browser, username, email)
        print(f"{count} ~ Preenchendo formulário para {username} e {email}")
        time.sleep(random_time())
        src.webdriver.clickAmikaOption(browser, options_dict)
        time.sleep(random_time())
        src.webdriver.click_submit_button(browser)
        print(f"{count} ~ Clicando no botão de envio para {username} e {email}")
        time.sleep(random_time())
        browser.close()
        print(f"{count} ~ Executado para {username} e {email}")
        print("="*50)
    end = time.time()
    print(f"\nTempo de execução: {time.strftime('%H:%M:%S', time.gmtime(end - start))}")

# MARK: - Main
if __name__ == '__main__':

    # Verificar se argumentos foram passados corretamente
    n = 1
    headless = False
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        n = int(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2] == "--headless":
        n = int(sys.argv[1])
        headless = True
    else:
        exit("usage: python3 amika_bot.py <n> [--headless]")
    
    # Enviar a solicitação
    send_request(n, headless)