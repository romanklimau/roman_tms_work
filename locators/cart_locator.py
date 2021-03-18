from selenium.webdriver.common.by import By


class CartLocator:

    LOCATOR_QUANTITY = (By.CSS_SELECTOR,
                        '.dataTable.rounded-corners > tbody > tr:nth-child(2)'
                        ' > td:nth-child(1)')
    LOCATOR_TOTAL_PRICE = (By.CSS_SELECTOR, '.dataTable.rounded-corners >'
                                            ' tbody > tr:nth-child(2) >'
                                            ' td:nth-child(6)')
    LOCATOR_PAYMENT = (By.CSS_SELECTOR, '.footer > td:nth-child(2) > strong')
    LOCATOR_BUTTON_CONFIRM_ORDER = (By.XPATH,
                                    '//button[@name="confirm_order"]/..')
    LOCATOR_ORDER_SUCCESSFULLY = (By.XPATH, '//h1[@class="title"]')
