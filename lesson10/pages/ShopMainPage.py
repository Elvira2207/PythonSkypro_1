from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopMainPage:
    def __init__(self, driver):
        """
        Конструктор класса ShopMainPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self._driver = driver

    @allure.step("Выбор товаров путем добавления их в корзину")
    def add_product(self):
        """
        Выбирается товар и добавляется в корзину
        :param add-to-cart: bool - кнопка для добавления товара в корзину
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        """
        Осуществляет переход в корзину
        """