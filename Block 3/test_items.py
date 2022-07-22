from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(link)
    browser.find_element(By.XPATH, ".//button[contains(@class, 'btn-add-to-basket')]")
    time.sleep(3)  # Just to check the language

# TO RUN USE - pytest -s -v --browser_name=chrome --language=ru test_items.py
