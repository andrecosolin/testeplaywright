from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/")
    page.get_by_label("E-mail ou número de telefone").click()
    page.get_by_label("E-mail ou número de telefone").fill("meuemail")
    page.get_by_label("Senha").click()
    page.get_by_label("Senha").fill("minhasenha")
    page.locator("form").filter(has_text="E-mail ou número de telefone Senha Exibir Esqueceu a senha? Entrar").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Photo of André Cosolin André Cosolin").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
