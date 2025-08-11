from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopMainPage:
    def __init__(self, browser):
        self._driver = browser

    def add_product(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

