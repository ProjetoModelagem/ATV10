import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ..pages.login_page import LoginPage
from ..pages.dashboard_page import DashboardPage

def _abrir_driver_ou_skip():
    try:
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return d
    except Exception as e:
        pytest.skip(f"Teste web POM pulado: Chrome indisponível ({e})")

@pytest.fixture
def driver():
    d = _abrir_driver_ou_skip()
    yield d
    d.quit()

def test_login_pom(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.abrir()
    login.fazer_login("student", "Password123")

    assert dashboard.esta_logado()
