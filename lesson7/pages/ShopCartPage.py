from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopCartPage:
    def __init__(self, browser):
        self._driver = browser

    def button_checkout(self):
        WebDriverWait(self._driver, 10).until(
          EC.element_to_be_clickable((By.ID, "checkout"))).click()