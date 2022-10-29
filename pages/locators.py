from selenium.webdriver.common.by import By


class NavbarLocators():
    NAVBAR_ABOUT = (By.XPATH, "//a[text()='About']")
    NAVBAR_DOWNLOADS = (By.XPATH, "//span[text()='Downloads']")
    NAVBAR_DOCUMENTATION = (By.XPATH, "//span[text()='Documentation']")
    NAVBAR_PROJECTS = (By.XPATH, "//span[text()='Projects']")
    NAVBAR_SUPPORT = (By.XPATH, "//span[text()='Support']")
    NAVBAR_BLOG = (By.XPATH, "//span[text()='Blog']")
    NAVBAR_LANG = (By.XPATH, "//a[text()='English']")
    NAVBAR_ABOUT_SEL = (By.XPATH, '//*[@id="main_navbar"]/ul/li[2]/div/a[1]')
