import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def _abrir_driver_ou_skip():
    try:
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return d
    except Exception as e:
        pytest.skip(f"Busca Google pulada: Chrome indisponível ({e})")

@pytest.fixture
def chrome_driver():
    driver = _abrir_driver_ou_skip()
    yield driver
    driver.quit()

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
])
def test_busca_google(chrome_driver, termo_busca):
    chrome_driver.get("https://www.google.com")

    box = chrome_driver.find_element(By.NAME, "q")
    box.send_keys(termo_busca)
    box.submit()

    # espera simples só pra garantir que carregou resultado
    time.sleep(2)

    # checa se o termo apareceu nos resultados
    assert termo_busca.lower() in chrome_driver.page_source.lower()
