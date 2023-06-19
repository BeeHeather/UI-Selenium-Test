from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(URL)

input_login = driver.find_element(By.ID, "user-name")
input_password = driver.find_element(By.ID, "password")
start_button = driver.find_element(By.ID, "login-button")

input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)
start_button.click()
pass