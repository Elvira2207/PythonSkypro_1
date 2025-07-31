from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopLoginPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self._driver.implicitly_wait(4)

    def data_entry(self):
        username_input = self._driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self._driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        Login_button = self._driver.find_element(By.ID, "login-button").click()