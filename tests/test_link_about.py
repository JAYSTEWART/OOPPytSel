import time

from selenium import webdriver

from pages.login_page import Login_page
from pages.main_page import Main_page


def test_link_about():
    driver = webdriver.Chrome()

    print('Start Test')

    login = Login_page(driver)
    login.autorizathion()

    mp = Main_page(driver)
    mp.select_menu_about()

    print('Finish test')
    time.sleep(5)
