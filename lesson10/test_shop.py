import allure
from selenium import webdriver
from pages.ShopPage import ShopPage

@allure.title("Тестирование магазина")
@allure.feature("Интернет-магазин")
@allure.description("Тест проверяет корректность работы магазина. "
                    "Страницы авторизации, добавление товара в корзину, корзина")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_validation():
    browser = webdriver.Firefox()
    login_page = ShopPage(browser)
    with allure.step("Открытие страницы входа в интернет-магазин"):
        login_page.open()
    with allure.step("Ввод данных для авторизации {user-name}: {password}:{login-button}"):
        login_page.data_entry()

    main_page = ShopPage(browser)
    with allure.step("Выбор товаров путем добавления их в корзину"):
        main_page.add_product()

    cart_page = ShopPage(browser)
    with allure.step("Нажатие кнопки {checkout}"):
        cart_page.button_checkout()

    order_page = ShopPage(browser)
    with allure.step("Информация о пользователе {first-name}: {last-name}: {postal-code}: {continue}"):
        order_page.an_order()
    with allure.step("Открытие итоговой суммы корзины"):
        order_page.total_price()

    browser.quit()