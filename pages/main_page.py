from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    product_3 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    cart = "//div[@id='shopping_cart_container']"
    button_menu = "//button[@id='react-burger-menu-btn']"
    button_about = "//a[@id='about_sidebar_link']"

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_button_menu(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_menu)))

    def get_about(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_about)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu(self):
        self.get_button_menu().click()
        print('Click menu')

    def click_about(self):
        self.get_about().click()
        print('Click About')

    # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about()
        self.assert_url('https://saucelabs.com/')
