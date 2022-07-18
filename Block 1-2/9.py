from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

localor = (By.ID, "verify")
button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(localor))

# Сделал отдельно локатор, чтобы показать, зачем в строчке ниже (закоменченой) нужны двойные скобки.
# Дело в том, что в element_located ожидается локатор, который является кортежем, а кортеж должен содержать скобки,
# поэтому одни скобки для передачи аргумента, а другие от переданного кортежа
# button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "verify")))
button.click()
button = WebDriverWait(browser, 5).until_not(
    EC.element_to_be_clickable((By.ID, "verify"))
)
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
browser.quit()
