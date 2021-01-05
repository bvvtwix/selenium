from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure_el = browser.find_element_by_id("treasure")
    treasure = treasure_el.get_attribute("valuex")
    treasure_x = calc(treasure)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(treasure_x)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    peopleRule = browser.find_element_by_id("robotsRule")
    peopleRule.click()

    submit_button = browser.find_element_by_css_selector("button")
    submit_button.click()


finally:
    time.sleep(4)
    browser.quit()