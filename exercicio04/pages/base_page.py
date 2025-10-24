class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def digitar(self, locator, texto):
        self.driver.find_element(*locator).send_keys(texto)

    def clicar(self, locator):
        self.driver.find_element(*locator).click()
