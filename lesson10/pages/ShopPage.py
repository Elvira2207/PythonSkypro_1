from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopPage:
    def __init__(self, driver):
        """
        Конструктор класса ShopPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self._driver = driver
        self._driver.implicitly_wait(4)

    @allure.step("Открытие страницы входа в интернет-магазин")
    def open(self):
        self._driver.get("https://www.saucedemo.com")

    @allure.step("Ввод данных для авторизации {user-name}: {password}:{login-button}")
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
    @allure.step("Нажатие кнопки {checkout}")
    def button_checkout(self):
        """
        Нажимает на кнопку проверки списка товара в корзине
        """
        WebDriverWait(self._driver, 10).until(
          EC.element_to_be_clickable((By.ID, "checkout"))).click()

    @allure.step("Информация о пользователе {first-name}: {last-name}: {postal-code}: {continue}")
    def an_order(self):
        """
        Вводит данные о пользователе и индекс доставки
        :param first-name: str - имя пользователя
        :param last-name: str - фамилия пользователя
        :param postal-code: int - индекс
        :param continue: bool - кнопка подтверждения данных
        """
        firstname = self._driver.find_element(By.ID, "first-name")
        firstname.send_keys("Elvira")
        lastname = self._driver.find_element(By.ID, "last-name")
        lastname.send_keys("Kim")
        zip_code = self._driver.find_element(By.ID, "postal-code")
        zip_code.send_keys("680031")
        button = self._driver.find_element(By.ID, "continue").click()

    @allure.step("Открытие итоговой суммы корзины")
    def total_price(self):
        """
        Открывается список выбранных товаров с общей суммой
        :param expected_total: int - ожидаемый результат
        :return: total_value - общая сумма
        """
        total_element = self._driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_value = float(total_text.split("$")[1])
        expected_total = 58.29
        assert total_value == expected_total, (
            f"Итоговая сумма составляет ${total_value:.2f}, "
            f"ожидалось ${expected_total:.2f}")