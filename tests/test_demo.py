from selenium.webdriver.common.by import By
import time
import allure 


@allure.epic('Allure Epic')
@allure.feature('Demo Feature')
@allure.story('Telegram bot run test')
@allure.issue('issue link')
@allure.testcase('Testcase')
class TestDemo:
    def test_yandex(self, browser):
        browser.get("https://www.yandex.ru/")
        time.sleep(2)
        browser.get("https://yandex.ru/search/?text=тинькофф")
        time.sleep(2)
        assert "тинькофф" in browser.title        

    # def test_yandex_search(self, browser):
    #     browser.get("https://yandex.ru/search/?text=тинькофф")
    #     time.sleep(2)
    #     assert "тинькофф" in browser.title