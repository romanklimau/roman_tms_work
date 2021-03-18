from selenium.webdriver.common.by import By


class LeftBarLocator:

    LOCATOR_FIELD_EMAIL = (By.XPATH, "//input[@name='email']")
    LOCATOR_FIELD_PASSWD = (By.XPATH, "//input[@name='password']")
    LOCATOR_BUTTON_LOGIN = (By.XPATH, "//button[@name='login']")
