from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop_validation():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    Login_button = driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()

    firstname = driver.find_element(By.ID, "first-name")
    firstname.send_keys("Elvira")
    lastname = driver.find_element(By.ID, "last-name")
    lastname.send_keys("Kim")
    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("680031")
    button = driver.find_element(By.ID, "continue").click()

# total = driver.find_element(By.CLASS_NAME, "summary_total_label").get_attribute("class")
# assert 'summary_total_label' == "$58.29"
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_value = float(total_text.split("$")[1])

    # Проверка итоговой суммы
    expected_total = 58.29
    assert total_value == expected_total, (
    f"Итоговая сумма составляет ${total_value:.2f}, "
    f"ожидалось ${expected_total:.2f}")

    driver.quit()