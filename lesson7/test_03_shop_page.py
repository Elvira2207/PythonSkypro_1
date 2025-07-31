
from selenium import webdriver
from pages.ShopLoginPage import ShopLoginPage
from pages.ShopMainPage import ShopMainPage
from pages.ShopCartPage import ShopCartPage
from pages.ShopOrderPage import ShopOrderPage

def test_shop_validation():
    browser = webdriver.Firefox()
    login_page = ShopLoginPage(browser)
    login_page.data_entry()

    main_page = ShopMainPage(browser)
    main_page.add_product()

    cart_page = ShopCartPage(browser)
    cart_page.button_checkout()

    order_page = ShopOrderPage(browser)
    order_page.an_order()
    order_page.total_price()

    browser.quit()






