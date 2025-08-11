from selenium.webdriver.common.by import By

class ShopOrderPage:
    def __init__(self, browser):
        self._driver = browser

    def an_order(self):
        firstname = self._driver.find_element(By.ID, "first-name")
        firstname.send_keys("Elvira")
        lastname = self._driver.find_element(By.ID, "last-name")
        lastname.send_keys("Kim")
        zip_code = self._driver.find_element(By.ID, "postal-code")
        zip_code.send_keys("680031")
        button = self._driver.find_element(By.ID, "continue").click()

    def total_price(self):
        total_element = self._driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_value = float(total_text.split("$")[1])
        expected_total = 58.29
        assert total_value == expected_total, (
            f"Итоговая сумма составляет ${total_value:.2f}, "
            f"ожидалось ${expected_total:.2f}")