from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from sql_db.db_litecart_sql import Sql_DB


def test_opportunity_to_make_an_order(browser, email_data, password_data):
    main_page = MainPage(browser)
    main_page.login(email_data, password_data)
    main_page.open_product_page()
    product_page = ProductPage(browser)
    product_page.add_duck_in_cart()
    main_page.open_page_cart()
    cart_page = CartPage(browser)
    cart_page.checking_price()
    cart_page.checking_quntity_product()
    # database = Sql_DB()
    # id_in_database_before = database.return_len_orders(database.connect())
    cart_page.make_order()
    cart_page.checking_maked_order()
    # id_in_database_later = database.return_len_orders(database.connect())
    # database.comarison_id_order(id_in_database_before, id_in_database_later)
