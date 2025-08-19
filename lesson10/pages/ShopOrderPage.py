from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopOrderPage:
    def __init__(self, driver):
        """
        Конструктор класса ShopOrderPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self._driver = driver

    @allure.step("Информация о пользователе first-name: last-name: postal-code: continue")
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