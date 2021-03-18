from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple, time=60):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f'Не найден локатор: {locator}')

    def find_elements(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f'Can not find element {locator}')
