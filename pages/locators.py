from selenium.webdriver.common.by import By


class NavbarLocators():
    NAVBAR_ABOUT = (By.XPATH, "//a[text()='About']")
    NAVBAR_DOWNLOADS = (By.XPATH, "//span[text()='Downloads']")
    NAVBAR_DOCUMENTATION = (By.XPATH, "//span[text()='Documentation']")
    NAVBAR_PROJECTS = (By.XPATH, "//span[text()='Projects']")
    NAVBAR_SUPPORT = (By.XPATH, "//span[text()='Support']")
    NAVBAR_BLOG = (By.XPATH, "//span[text()='Blog']")
    NAVBAR_LANG = (By.XPATH, "//a[text()='English']")
    NAVBAR_ABOUT_SEL = (By.XPATH, "//a[@class='dropdown-item'][text()='About Selenium']")
    NAVBAR_STRUCTURE = (By.XPATH, "//a[text() ='Structure and Governance']")
    NAVBAR_SEARCH = (By.XPATH, "//span[text()='Search']")
    NAVBAR_SEARCH_INPUT = (By.CSS_SELECTOR, ".DocSearch-Input")
