from pages.main_page import MainPage
from pages.regional_settings_page import RegionalSettings


def test_change_country_and_currency(browser, currency_data_config, country_data_config):
    currency = currency_data_config
    country = country_data_config

    main_page = MainPage(browser)
    main_page.open_window_regional_settings()
    regional_settings = RegionalSettings(browser)
    regional_settings.change_currency(currency)
    regional_settings.change_coutry(country)
    regional_settings.click_save_button()
    main_page.checking_currency()
    main_page.checking_country()
