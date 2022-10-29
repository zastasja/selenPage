from .pages.main_page import MainPage
from .pages.locators import NavbarLocators

link = "https://www.selenium.dev/"


def test_open_about_page(browser):
    page = MainPage(browser, link)
    page.open_mainPage()
    page.dropdown_menu()
    page.dropdown_menu_about()
    page.should_be_current_page(f'{link}about/')

def test_open_structure_page(browser):
    page = MainPage(browser, link)
    page.open_mainPage()
    page.dropdown_menu()
    page.dropdown_menu_structure()
    page.should_be_current_page(f'{link}project/')

def test_open_downloads(browser):
    page = MainPage(browser, link)
    page.open_mainPage()
    page.click_element(*NavbarLocators.NAVBAR_DOWNLOADS)
    page.should_be_current_page(f'{link}downloads/')

def test_open_projects(browser):
    page = MainPage(browser, link)
    page.open_mainPage()
    page.click_element(*NavbarLocators.NAVBAR_PROJECTS)
    page.should_be_current_page(f'{link}projects/')

def test_open_support(browser):
    page = MainPage(browser, link)
    page.open_mainPage()
    page.click_element(*NavbarLocators.NAVBAR_SUPPORT)
    page.should_be_current_page(f'{link}support/')

def test_open_blog(browser):
    page = MainPage(browser, link)
    page.open_mainPage()
    page.click_element(*NavbarLocators.NAVBAR_BLOG)
    page.should_be_current_page(f'{link}blog/')