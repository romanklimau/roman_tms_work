from pages.base_page import BasePage
from locators.duck_locator import ProductDuckLocator
from selenium.webdriver.support.ui import Select

class ProductPage(BasePage):

    def add_duck_in_cart(self):
        try:
            select_size = Select(self.find_element(
                ProductDuckLocator.LOCATOR_SELECT_SIZE_DUCK
            ))
            select_size.select_by_index(1)

        finally:

            quantity_duck = self.find_element(
                ProductDuckLocator.LOCATOR_SELECT_QUANTITY_DUCK
            )
            quantity_duck.clear()
            quantity_duck.send_keys(3)
            add_duck = self.find_element(
                ProductDuckLocator.LOCATOR_BUTTON_ADD_TO_CART
            )
            add_duck.click()
            self.checking_elements_after_adding(
                ProductDuckLocator.LOCATOR_QUANTITY_DUCK_IN_CAR_ON_THE_DUCK_PAGE)
