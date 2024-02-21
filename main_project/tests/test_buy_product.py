import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.pages.cart_page import Cart_page
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page


def test_buy_product():
    driver = webdriver.Chrome()

    print('Start Test')

    login = Login_page(driver)
    login.autorizathion()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    time.sleep(5)
