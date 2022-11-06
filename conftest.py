import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope='function')
def browser():
    o = webdriver.ChromeOptions()
    o.headless = True
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    browser.quit()
