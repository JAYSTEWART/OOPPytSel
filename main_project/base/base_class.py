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
