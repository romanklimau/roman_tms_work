from pages.base_page import BasePage
from locators.cart_locator import CartLocator


class CartPage(BasePage):

    def checking_price(self):
        price_duck = self.find_element(
            CartLocator.LOCATOR_TOTAL_PRICE
        ).text
        price_order = self.find_element(
            CartLocator.LOCATOR_PAYMENT
        ).text
        assert price_duck == price_order, f'{price_duck}' \
                                          f' is not eq {price_order}'

    def checking_quntity_product(self):
        q = self.find_element(
            CartLocator.LOCATOR_QUANTITY
        ).text
        quantity_on_the_page = int(q)
        assert quantity_on_the_page == 3, f'Quantity ducks -' \
                                          f' {quantity_on_the_page} is not eq 3'

    def make_order(self):
        button_confirm_order = self.find_element(
            CartLocator.LOCATOR_BUTTON_CONFIRM_ORDER
        )
        button_confirm_order.click()
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        visible_confirm_order = self.checking_confirm_order(
            CartLocator.LOCATOR_ORDER_SUCCESSFULLY)
        assert visible_confirm_order is True, f'{visible_confirm_order}, not found'
