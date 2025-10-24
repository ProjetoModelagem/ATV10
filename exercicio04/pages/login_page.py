from selenium.webdriver.common.by import By
from .base_page import BasePage  # import relativo pro mesmo pacote "pages"

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")

    def abrir(self):
        # Abre a página de login usada no exercício
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def fazer_login(self, usuario: str, senha: str):
        # Preenche usuário e senha e clica em Login
        self.digitar(self.USERNAME, usuario)
        self.digitar(self.PASSWORD, senha)
        self.clicar(self.SUBMIT)
