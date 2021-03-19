from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple, time=30):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f'Не найден локатор: {locator}')

    def find_elements(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f'Can not find element {locator}')

    def checking_elements_after_adding(self, locator: tuple, time=30):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text_='3'),
            message=f'Can not change value {locator}')

    def checking_confirm_order(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text_='Your order is successfully completed!'),
            message=f'Can not change value {locator}')
