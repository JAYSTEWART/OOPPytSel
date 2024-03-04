import time

import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.user_information_page import User_information_page


@pytest.mark.order(3)
def test_buy_product_1():
    driver = webdriver.Chrome()

    print('Start Test')

    login = Login_page(driver)
    login.autorizathion()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    # uip = User_information_page(driver)
    # uip.input_data()
    #
    # pp = Payment_page(driver)
    # pp.payment()
    #
    # fp = Finish_page(driver)
    # fp.finish()
    print('Finish test 1')
    time.sleep(5)


@pytest.mark.order(1)
def test_buy_product_2():
    driver = webdriver.Chrome()

    print('Start Test 2')

    login = Login_page(driver)
    login.autorizathion()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    # uip = User_information_page(driver)
    # uip.input_data()
    #
    # pp = Payment_page(driver)
    # pp.payment()
    #
    # fp = Finish_page(driver)
    # fp.finish()
    print('Finish test 2')
    time.sleep(5)


@pytest.mark.order(2)
def test_buy_product_3():
    driver = webdriver.Chrome()

    print('Start Test 3')

    login = Login_page(driver)
    login.autorizathion()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    # uip = User_information_page(driver)
    # uip.input_data()
    #
    # pp = Payment_page(driver)
    # pp.payment()
    #
    # fp = Finish_page(driver)
    # fp.finish()
    print('Finish test 3')
    time.sleep(5)
