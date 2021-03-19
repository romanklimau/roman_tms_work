from selenium.webdriver.common.by import By


class MainPageLocator:
    LOCATOR_DUCK = (By.XPATH, "//div[@class='image-wrapper']")
    LOCATOR_YELLOW_DUCK = (By.XPATH, '//div[@id="box-campaigns"]'
                                     '//li[@class="product column'
                                     ' shadow hover-light"]')
