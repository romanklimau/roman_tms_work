from selenium.webdriver.common.by import By


class AddBarLocator:

    LOCATOR_CHANGE_REGIONAL_SETTINGS = (By.XPATH, '//div[@class="change"]')
    LOCATOR_CURRENCY = (By.XPATH, '//div[@class="currency"]')
    LOCATOR_COUNTRY = (By.XPATH, '//div[@class="country"]')
    LOCATOR_QUNTITY_PRODUCT_IN_CART = (By.XPATH, '//span[@class="quantity"]')
    LOCATOR_OPEN_PAGE_CART = (By.XPATH, "//strong[text()='Cart:']")

