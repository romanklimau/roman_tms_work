from pages.base_page import BasePage
from locators.regional_settings_locator import RegionalSettingsLocator
from selenium.webdriver.support.ui import Select


class RegionalSettings(BasePage):

    def change_currency(self, currency):
        locator = RegionalSettingsLocator()
        change_currency_locator = Select(self.find_element(locator.CURRENCY_LIST_LOCATOR))
        change_currency_locator.select_by_visible_text(currency)

    def change_coutry(self, country):
        locator = RegionalSettingsLocator()
        change_country_locator = Select(self.find_element(locator.COUNTRY_LIST_LOCATOR))
        change_country_locator.select_by_visible_text(country)

    def click_save_button(self):
        self.driver.implicitly_wait(20)
        button_save = self.find_element(
            RegionalSettingsLocator.BUTTON_SAVE_LOCATOR
        )
        button_save.click()

