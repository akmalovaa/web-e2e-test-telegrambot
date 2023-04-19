from selenium.webdriver.common.by import By
import time
import allure 


@allure.epic('Allure Epic')
@allure.feature('Demo Feature')
@allure.story('Passed Example')
@allure.issue('https://example.org/issue/1')
@allure.testcase('https://example.org/tms/2')
class TestDemo:
    def test_yandex_demo(self, browser):
        browser.get("https://www.yandex.ru/")
        time.sleep(2)
        assert "Дзен" in browser.title


    def test_search(self, browser):
        browser.get("https://yandex.ru/search/?text=тинькофф")
        time.sleep(2)
        assert "тинькофф" in browser.title