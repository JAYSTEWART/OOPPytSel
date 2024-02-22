from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.base.base_class import Base


class User_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Generation of fake data
    fake = Faker()
    first_name_fake = fake.first_name()
    last_name_fake = fake.last_name()
    zip_code_fake = fake.postcode()

    # Locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    continu = "//input[@name='continue']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continu)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input Zip Code")

    def click_continue(self):
        self.get_continue().click()
        print("Click continue")

    # Methods

    def input_data(self):
        self.get_current_url()
        self.input_first_name(self.first_name_fake)
        self.input_last_name(self.last_name_fake)
        self.input_zip_code(self.zip_code_fake)
        self.click_continue()
