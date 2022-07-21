import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


def answer():
    return math.log(int(time.time()))


@pytest.fixture()
def browser():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_param_task(browser, url):
    browser.get(f"{url}")
    text_area = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    text_area.send_keys(answer())
    submit = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission")))
    submit.click()
    text = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    assert text == "Correct!"
