from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    num1_el = browser.find_element_by_id("num1")
    num1 = num1_el.text
    num2_el = browser.find_element_by_id("num2")
    num2 = num2_el.text
    sum = int(num1) + int(num2)

    dropdown = Select(browser.find_element_by_id("dropdown"))
    dropdown.select_by_value(str(sum))

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(4)
    browser.quit()