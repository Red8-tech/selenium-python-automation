from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import Logger


class HomePage(BasePage):

    HOME_LOGO = (By.CSS_SELECTOR, "#logo")
    MY_ACCOUNT_LINK = (By.XPATH, "//span[contains(normalize-space(), 'My Account')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(normalize-space(), 'Login')]")
    PRODUCTS_LINK = (By.XPATH, "//a[contains(normalize-space(), 'Desktops')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger("HomePage")

    def open_home_page(self):
        self.logger.info("Opening home page")
        self.open_url(self.config.get("base_url"))

    def is_home_page_displayed(self):
        self.logger.info("Verifying home page is displayed")
        self.logger.info(f"Current URL: {self.driver.current_url}")
        self.logger.info(f"Page title: {self.driver.title}")
        
        return self.find_element(self.HOME_LOGO).is_displayed()

    def click_login(self):
        self.logger.info("Opening My Account menu")
        self.click(self.MY_ACCOUNT_LINK)

        self.logger.info("Clicking Login")
        self.click(self.LOGIN_LINK)

    def click_products(self):
        self.logger.info("Clicking Desktops")
        self.click(self.PRODUCTS_LINK)

    def is_logged_in(self):
        self.logger.info("Verifying user is logged in")
        return self.find_element(
            (By.XPATH, "//a[contains(normalize-space(), 'My Account')]")
        ).is_displayed()
