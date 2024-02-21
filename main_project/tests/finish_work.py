# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from main_project.pages.login_page import Login_page
#
#
# class Test_1:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get('https://www.saucedemo.com/')
#         print('Start Test')
#
#     def test_select_product(self):
#         login_all = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'locked_out_user']
#         password_all = 'secret_sauce'
#         # Запуск цикла для прогона всех аккаунтов
#         for i in login_all:
#             login = Login_page(self.driver)
#             login.autorizathion(i, password_all)
#
#             # Поиск сообщения о блокировке аккаунта
#             try:
#                 locked_out_message = WebDriverWait(self.driver, 1).until(
#                     EC.visibility_of_element_located(
#                         (By.XPATH, '//div[@id="login_button_container"]/div/form/div[3]'))).text
#                 if locked_out_message == 'Epic sadface: Sorry, this user has been locked out.':
#                     print(f'Sorry, this {i.upper()} has been locked out.\n')
#                     self.driver.refresh()
#                     continue
#             except TimeoutException:
#                 pass
#             # Опредление главное страницы и выход из аккаунта
#             try:
#                 check_page = WebDriverWait(self.driver, 6).until(
#                     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Products')]"))).text
#                 if check_page == 'Products':
#                     print(f'Successful entry: {i}\n')
#                     back_page = WebDriverWait(self.driver, 1).until(
#                         EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
#                     back_page.click()
#                     logout = WebDriverWait(self.driver, 1).until(
#                         EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
#                     logout.click()
#                     self.driver.refresh()
#                     continue
#             except TimeoutException:
#                 pass
#
#         self.driver.quit()
#
#
# test = Test_1()
# test.test_select_product()
