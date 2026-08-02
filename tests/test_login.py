from pages.login_page import LoginPage
from playwright.sync_api import Page, expect
def test_login_com_sucesso(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    def test_login_usuario_invalido(page: Page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("usuario_falso", "senha_errada")
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Username and password do not match")