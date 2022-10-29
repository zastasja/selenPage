from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.locators import NavbarLocators

link = "https://www.selenium.dev/"


def test_open_about(browser):
    page = MainPage(browser, link)
    page.go_to_about_page()