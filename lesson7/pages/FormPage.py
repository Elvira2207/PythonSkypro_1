from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def fill_field(self):
        self._driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self._driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self._driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self._driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        self._driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self._driver.find_element(By.NAME, "city").send_keys("Москва")
        self._driver.find_element(By.NAME, "country").send_keys("Россия")
        self._driver.find_element(By.NAME, "job-position").send_keys("QA")
        self._driver.find_element(By.NAME, "company").send_keys("SkyPro")
    def button_click(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def check_field_color(self):
        zip_code_field = self._driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert zip_code_field == "alert py-2 alert-danger"
        fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position",
                  "#company"]
        for field in fields:
            field = self._driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")
            assert field == "alert py-2 alert-success"
