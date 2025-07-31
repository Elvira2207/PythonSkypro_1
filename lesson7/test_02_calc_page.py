from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalcPage import CalcPage


def test_slow_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_page = CalcPage(browser)
    calc_page.input_delay()
    calc_page.calc_buttons()
    calc_page.check_result()

    browser.quit()