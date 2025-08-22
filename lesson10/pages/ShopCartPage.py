from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopCartPage:
    def __init__(self, driver):
        """
        Конструктор класса ShopCartPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self._driver = driver

    @allure.step("Нажатие кнопки checkout")
    def button_checkout(self):
        """
        Нажимает на кнопку проверки списка товара в корзине
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))).click()