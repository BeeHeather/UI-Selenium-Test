from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# defined parameters
URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def open_page(driver, URL):
    driver.get(URL)


def get_element_by_id(driver, id):
    element = driver.find_element(By.ID, id)
    return element


def element_send_keys(driver, id, type):
    element = get_element_by_id(driver, id)
    element.send_keys(type)


def button_click(driver, id):
    button = get_element_by_id(driver, id)
    button.click()


def login(driver, name, password, name_id):
    get_element_by_id(driver, name_id)
    get_element_by_id(driver, 'password')
    element_send_keys(driver, name_id, name)
    element_send_keys(driver, 'password', password)


driver = get_driver()
open_page(driver, URL)
login(driver=driver, name=LOGIN, password=PASSWORD, name_id='user-name')
button_click(driver, 'login-button')

driver.quit()