from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    inputs = browser.find_elements(By.XPATH, "//input[@type='text']")
    for input in inputs:
        input.send_keys('Random')
    add_file = browser.find_element(By.ID, "file")
    add_file.send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    browser.quit()
