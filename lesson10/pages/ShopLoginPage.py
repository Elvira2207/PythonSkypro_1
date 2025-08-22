from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopLoginPage:
    def __init__(self, driver):
        """
        Конструктор класса ShopLoginPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self._driver = driver

    @allure.step("Открытие страницы входа в интернет-магазин")
    def open(self):
        self._driver.get("https://www.saucedemo.com")

    @allure.step("Ввод данных для авторизации user-name: password: login-button")
    def data_entry(self):
        """
        Вводит данные для авторизации пользователя
        :param user-name: str - логин
        :param password: str - пароль
        :param login-button: bool - нажимает на кнопку подтверждения авторизации, после чего переходит на страницу товаров
        """
        username_input = self._driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self._driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        Login_button = self._driver.find_element(By.ID, "login-button").click()
