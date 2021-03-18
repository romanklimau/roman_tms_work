import random
from pages.base_page import BasePage
from locators.add_bar_locator import AddBarLocator
from locators.left_bar_locator import LeftBarLocator
from locators.main_page_locator import MainPageLocator

class MainPage(BasePage):

    def open_window_regional_settings(self):
        button_change = self.find_element(
            AddBarLocator.LOCATOR_CHANGE_REGIONAL_SETTINGS
        )
        button_change.click()

    def checking_currency(self):
        currency = self.find_element(
            AddBarLocator.LOCATOR_CURRENCY
        ).text
        assert 'EUR' == currency, f'{currency} not eq Euros'

    def checking_country(self):
        country = self.find_element(
            AddBarLocator.LOCATOR_COUNTRY
        ).text
        assert "Hong Kong" == country, f'{country} not eq Hong Kong'

    def login(self, email, password):
        field_email = self.find_element(
            LeftBarLocator.LOCATOR_FIELD_EMAIL
        )
        field_email.send_keys(email)
        field_password = self.find_element(
            LeftBarLocator.LOCATOR_FIELD_PASSWD
        )
        field_password.send_keys(password)
        button_login = self.find_element(
            LeftBarLocator.LOCATOR_BUTTON_LOGIN
        )
        button_login.click()

    def open_product_page(self):
        number_product = random.choice([1, 2, 3, 4, 5])
        product_duck = self.find_elements(
            MainPageLocator.LOCATOR_DUCK
        )
        duck = product_duck[number_product]
        duck.click()

    def open_page_cart(self):
        open_page_cart = self.find_element(
                AddBarLocator.LOCATOR_OPEN_PAGE_CART
            )
        open_page_cart.click()
