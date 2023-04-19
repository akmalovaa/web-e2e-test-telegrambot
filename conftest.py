import os
import time
from datetime import datetime

import allure
import pytest

from selenium import webdriver

# "videoCodec": "mpeg4",
@pytest.fixture(scope="function")
def browser(browser_name, request, message_id):
    selenoid_options = {"enableVNC": False,
                        "enableVideo": True,
                        "videoName": f'{message_id}.mp4',
                        "enableLog": False}
    if browser_name == "chrome":
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument('--ignore-ssl-errors=yes')
        browser_options.add_argument('--ignore-certificate-errors')
        browser_options.set_capability("selenoid:options", selenoid_options)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=browser_options
        )

    elif browser_name == "firefox":
        browser_options = webdriver.FirefoxOptions()
        browser_options.set_capability("selenoid:options", selenoid_options)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=browser_options
        )
    elif browser_name == "local":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Invalid browser name")

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="append",
        default=[],
        help="list of browser to pass to test functions",
    )
    parser.addoption(
        "--message_id",
        action="append",
        default=[],
        help="telegram message id",
    )



def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        metafunc.parametrize("browser_name", metafunc.config.getoption("browser_name"))
    if "message_id" in metafunc.fixturenames:
        metafunc.parametrize("message_id", metafunc.config.getoption("message_id"))

# it is this function that takes the screenshot in case of failures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
