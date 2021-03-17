from selenium.webdriver.common.by import By


class RegionalSettingsLocator:


    CURRENCY_LIST_LOCATOR = (By.XPATH, "//select[@name='currency_code']")
    COUNTRY_LIST_LOCATOR = (By.XPATH, "//select[@name='country_code']")
    BUTTON_SAVE_LOCATOR = (By.XPATH, '//button[@name="save"]')
