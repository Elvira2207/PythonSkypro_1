from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v138.dom import get_attributes
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_fill_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполнение формы

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

# Нажатие кнопки
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert zip_code_field == "alert py-2 alert-danger"
    fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"]
    for field in fields:
        field = driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")
        assert field == "alert py-2 alert-success"

    driver.quit()
