from selenium.webdriver.common.by import By


class ProductDuckLocator:
    LOCATOR_BUTTON_ADD_TO_CART = (By.XPATH, '//button[@name="add_cart_product"]')
    LOCATOR_SELECT_SIZE_DUCK = (By.XPATH,'//select[@name="options[Size]"]')
    LOCATOR_SELECT_SIZE_DUCK_SMALL = (By.XPATH, "//option[@value='Small']")
    LOCATOR_SELECT_QUANTITY_DUCK = (By.XPATH, '//input[@type="number"]')
