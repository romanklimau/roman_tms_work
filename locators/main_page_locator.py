from selenium.webdriver.common.by import By


class MainPageLocator:

    LOCATOR_REGIONAL_SETTINGS = (By.XPATH, '//li/a[@href="http://localhost/'
                                           'litecart/en/regional_settings"]')
    LOCATOR_CURRENCY = (By.XPATH, "//span[text()='EUR']")
    LOCATOR_COUNTRY = (By.CSS_SELECTOR, ".country")
