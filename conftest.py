import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")

# def init_chrome_browser():
#     o = webdriver.ChromeOptions()
#     o.headless = True
#     browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield browser
#     browser.quit()


def browser():
    o = webdriver.FirefoxOptions()
    o.headless = True
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield browser
    browser.quit()
