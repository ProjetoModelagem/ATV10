import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def _abrir_driver_ou_skip():
    """
    Tenta abrir o Chrome. Se não conseguir (sem Chrome instalado, etc.),
    pula o teste em vez de dar erro.
    """
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return driver
    except Exception as e:
        pytest.skip(f"Teste web pulado: Chrome indisponível ({e})")

@pytest.fixture
def chrome_driver():
    driver = _abrir_driver_ou_skip()
    yield driver
    driver.quit()

def test_login_sucesso(chrome_driver):
    chrome_driver.get("https://practicetestautomation.com/practice-test-login/")
    chrome_driver.find_element(By.ID, "username").send_keys("student")
    chrome_driver.find_element(By.ID, "password").send_keys("Password123")
    chrome_driver.find_element(By.ID, "submit").click()

    assert "Logged In Successfully" in chrome_driver.page_source

def test_login_senha_incorreta(chrome_driver):
    chrome_driver.get("https://practicetestautomation.com/practice-test-login/")
    chrome_driver.find_element(By.ID, "username").send_keys("student")
    chrome_driver.find_element(By.ID, "password").send_keys("errada")
    chrome_driver.find_element(By.ID, "submit").click()

    assert "Your password is invalid!" in chrome_driver.page_source
