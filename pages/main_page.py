from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator
from locators.add_bar_locator import AddBarLocator

class MainPage(BasePage):

    def open_window_regional_settings(self):
        button_change = self.find_element(
            AddBarLocator.LOCATOR_CHANGE_REGIONAL_SETTINGS
        )
        button_change.click()

    def checking_currency(self):
        currency = self.find_element(
            MainPageLocator.LOCATOR_CURRENCY
        ).text
        assert 'EUR' == currency, 'currency not changed'

    def checking_country(self):
        country = self.find_element(
            MainPageLocator.LOCATOR_COUNTRY
        ).text
        assert self.country == country, 'country not changed'
