import time

from selenium import webdriver
from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.user_information_page import User_information_page


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

    pp = Payment_page(driver)
    pp.payment()

    fp = Finish_page(driver)
    fp.finish()
    time.sleep(5)
