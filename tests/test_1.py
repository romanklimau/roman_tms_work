from pages.main_page import MainPage
from pages.regional_settings_page import RegionalSettings
from time import sleep


def test_change_country_and_currency(browser):
    data_usd = 'EUR'
    main_page = MainPage(browser)
    main_page.open_window_regional_settings()
    sleep(3)
    regional_settings = RegionalSettings(browser)
    regional_settings.change_currency(data_usd)
    sleep(3)
    # regional_settings.change_country()
    # regional_settings.save_chnges()
    # main_page.checking_currency()
    # main_page.checking_country()
