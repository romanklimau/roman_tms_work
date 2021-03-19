from selenium import webdriver
import pytest
import json
import os.path

def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target


@pytest.fixture()
def browser():

    driver = webdriver.ChromeOptions()
    driver.add_argument('--no-sandbox')
    driver.add_argument('--headless')
    driver.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=driver)
    driver.maximize_window()
    driver.get('http://localhost/litecart')
    yield driver
    driver.quit()


@pytest.fixture()
def currency_data_config():
    config_data_currency = load_config('recources/currency_data.json')
    return config_data_currency['EUR']


@pytest.fixture()
def country_data_config():
    config_data_country = load_config('recources/country_data.json')
    return config_data_country['HK']

@pytest.fixture()
def email_data():
    email = load_config('recources/user_data.json')
    return email['email']

@pytest.fixture()
def password_data():
    password = load_config('recources/user_data.json')
    return password['password']
