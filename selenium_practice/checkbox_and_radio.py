from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    time.sleep(1)

    x_el = browser.find_element_by_id("input_value")
    x = x_el.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    time.sleep(1)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

    robot_radio = browser.find_element_by_id("robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    assert robot_checked is None , "robot is not checked"

    robot_radio.click()
    time.sleep(1)

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()