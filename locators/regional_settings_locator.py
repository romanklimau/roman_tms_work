from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegionalSettingsLocator:

    def get_currency_locator(self):
        currency_locator = Select((By.XPATH, "//select[@name='currency_code']"))
        return currency_locator



    # LOCATOR_CHOISE_COUNTRY = (By.XPATH, '//span[@class="select2-selection'
    #                                     ' select2-selection--single"]')
    # LOCATOR_FIELD_CHANGE_COUNTRY = (By.CSS_SELECTOR, '.select2-search__field')
    # LOCATOR_COUNTRY_CHECKED = (By.XPATH, "//select[@name='country_code']/option[text()='Lithuania']")
    # LOCATOR_BUTTON_SAVE = (By.XPATH, "//button[@value='Save']")
