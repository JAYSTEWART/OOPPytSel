from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():

    def __init__(self, driver):
        self.driver = driver

    def autorizathion(self, login_name, password):
        username = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        username.send_keys(login_name)
        print('Input Login')

        user_password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        user_password.send_keys(password)
        print('Input Password')

        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print('Click Login Button')

