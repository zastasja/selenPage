from .base_page import BasePage
from .locators import NavbarLocators
from selenium.webdriver.common.by import By

# link = "https://www.selenium.dev/"


class MainPage(BasePage):

    def go_to_about_page():
        BasePage.open_page()
        assert "https://www.selenium.dev/" == BasePage.should_be_current_page(), 'wrong URL'
        BasePage.click_element(*NavbarLocators.NAVBAR_ABOUT)
        BasePage.click_element(*NavbarLocators.NAVBAR_ABOUT_SEL)


