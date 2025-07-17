from time import sleep

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.XPATH, '//input[@id="username"]')
username_input.send_keys("tomsmith")

sleep(3)

password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!")

sleep(3)

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

sleep(3)

message = driver.find_element(By.CSS_SELECTOR, '[data-alert=""]')
print_message = message.text
print(print_message)

driver.quit()

