from pages.base_page import BasePage
from locators.regional_settings_locator import RegionalSettingsLocator
from selenium.webdriver.support.ui import Select

class RegionalSettings(BasePage):

    def change_currency(self, currency):
        change_currency_locator = RegionalSettingsLocator()
        change_currency_locator.get_currency_locator.select_by_value(currency)



    # def change_country(self, country):
    #     list_country = self.find_element(
    #         RegionalSettingsLocator.LOCATOR_CHOISE_COUNTRY
    #     )
    #     list_country.click()
    #     field_country = self.find_element(
    #         RegionalSettingsLocator.LOCATOR_FIELD_CHANGE_COUNTRY
    #     )
    #     field_country.click()
    #
    # def check_country(self, country):
    #     field_country.send_keys(self.country)
    #     field_country_checked = self.find_element(
    #         RegionalSettingsLocator.LOCATOR_COUNTRY_CHECKED
    #     )
    #     field_country_checked.click()
    #
    # def click_save_button(self):
    #     buttono_save = self.find_element(
    #         RegionalSettingsLocator.LOCATOR_BUTTON_SAVE
    #     )
    #     buttono_save.click()
