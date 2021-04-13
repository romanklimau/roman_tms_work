from selenium import webdriver
import mysql.connector as mysql
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
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost/litecart')
    yield driver
    driver.quit()


@pytest.fixture()
def currency_data_config():
    config_data_currency = load_config('resources/currency_data.json')
    return config_data_currency['EUR']


@pytest.fixture()
def country_data_config():
    config_data_country = load_config('resources/country_data.json')
    return config_data_country['HK']

@pytest.fixture()
def email_data():
    email = load_config('resources/user_data.json')
    return email['email']

@pytest.fixture()
def password_data():
    password = load_config('resources/user_data.json')
    return password['password']

@pytest.fixture()
def db_connect():
    connect = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database='db_litecart'
    )
    yield connect
    connect.close()

@pytest.fixture()
def get_data_to_add_pet():
    new_pet_data = load_config('resources/new_pet.json')
    return new_pet_data

@pytest.fixture()
def del_added_pet():
    new_pet_data = load_config('resources/new_pet.json')
    return new_pet_data
