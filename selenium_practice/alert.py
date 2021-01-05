from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    input_value_el = browser.find_element_by_id("input_value")
    input_value = calc(input_value_el.text)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(input_value)

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    time.sleep(4)
    browser.quit()
