import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book = browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    button = browser.find_element(By.ID, 'solve')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
