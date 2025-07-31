from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v138.dom import get_attributes
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.FormPage import FormPage


def test_fill_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_page = FormPage(browser)
    form_page.fill_field()
    form_page.button_click()
    form_page.check_field_color()
    browser.quit()