from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
text_input = driver.find_element(By.XPATH, '//input[@type="text"]')
text_input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

button_name = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').text
print(button_name)

driver.quit()