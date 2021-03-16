from selenium import webdriver
import pytest


@pytest.fixture()
def browser():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost/litecart')
    yield driver
    driver.quit()
