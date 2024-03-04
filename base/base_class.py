import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    # Функция возврата URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL {get_url}')

    # Функция проверки значения текста на странице
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")  # дата , время
        self.driver.save_screenshot(
            f'D:\\Testing\\OOPPytSel\\main_project\\screen\\screenshot.{now_date}.png')  # делаем скриншот страницы
        print('Create screenshot')

    # Метод проверки URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value URL')
