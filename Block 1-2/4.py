from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("alert('Robots at work');")
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()



finally:
    time.sleep(3)
    browser.quit()