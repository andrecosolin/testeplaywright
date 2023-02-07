from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://www.hashtagtreinamentos.com/curso-python')
    pagina.fill('xpath=/html/body/div/div[2]/div/div[2]/form/div[1]/input', 'André')
    pagina.fill('xpath=/html/body/div/div[2]/div/div[2]/form/div[2]/input', 'yakira8815@uorak.com')
    pagina.fill('xpath=/html/body/div/div[2]/div/div[2]/form/div[3]/input', '16997031880')
    pagina.click('xpath=/html/body/div/div[2]/div/div[2]/form/button')
    time.sleep(10)



