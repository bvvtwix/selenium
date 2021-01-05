import os
from selenium import webdriver
import time

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    firstname = browser.find_element_by_css_selector("[name='firstname']")
    firstname.send_keys("Ivan")

    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("Petrov")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("ip@gmail.com")

    file = browser.find_element_by_id('file')
    file.send_keys(file_path)

    time.sleep(2)

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
