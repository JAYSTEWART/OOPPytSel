import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_1():
    @staticmethod
    def test_select_product():
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        # driver.maximize_window()

        print('Start Test')

        login_standard_user = 'standard_user'
        password_all = 'secret_sauce'

        login = Login_page(driver)
        login.autorizathion(login_standard_user, password_all)
        time.sleep(5)

        select_product = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('Click Select Product')

        enter_chopping_card = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '// div[ @ id = "shopping_cart_container"]')))
        enter_chopping_card.click()
        print('Click Enter Shopping Card')
        # time.sleep(3)

        succes_test = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]'))).text
        assert succes_test == 'Your Cart'
        print('Test succes')
        time.sleep(5)


test = Test_1
test.test_select_product()
