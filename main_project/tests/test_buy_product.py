import time

from selenium import webdriver
from main_project.pages.cart_page import Cart_page
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page
from main_project.pages.user_information_page import User_information_page


def test_buy_product():
    driver = webdriver.Chrome()

    print('Start Test')

    login = Login_page(driver)
    login.autorizathion()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    uip = User_information_page(driver)
    uip.input_data()
    time.sleep(5)
