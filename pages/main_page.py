from .base_page import BasePage
from .locators import NavbarLocators
from selenium.webdriver.common.by import By

link = "https://www.selenium.dev/"


class MainPage(BasePage):
    def open_mainPage(self):
        self.open_page()
        self.should_be_current_page(link)

    def dropdown_menu(self):
        self.click_element(*NavbarLocators.NAVBAR_ABOUT)

    def dropdown_menu_about(self):
        self.click_element(*NavbarLocators.NAVBAR_ABOUT_SEL)

    def dropdown_menu_structure(self):
        self.click_element(*NavbarLocators.NAVBAR_STRUCTURE)
