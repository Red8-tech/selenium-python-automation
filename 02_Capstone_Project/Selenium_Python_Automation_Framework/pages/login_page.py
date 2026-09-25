from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import Logger


class LoginPage(BasePage):

    MY_ACCOUNT_LINK = (
        By.XPATH,
        "//span[normalize-space()='My Account']"
    )

    LOGIN_LINK = (
        By.XPATH,
        "//div[@id='top-links']//a[normalize-space()='Login']"
    )

    EMAIL_INPUT = (
        By.ID,
        "input-email"
    )

    PASSWORD_INPUT = (
        By.ID,
        "input-password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//input[@value='Login']"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger("LoginPage")

    def open_login_page(self):

        self.logger.info("Opening login page")

        self.click(self.MY_ACCOUNT_LINK)
        self.click(self.LOGIN_LINK)

    def enter_email(self, email):

        self.logger.info("Entering email")

        self.enter_text(
            self.EMAIL_INPUT,
            email
        )

    def enter_password(self, password):

        self.logger.info("Entering password")

        self.enter_text(
            self.PASSWORD_INPUT,
            password
        )

    def click_login(self):

        self.logger.info("Clicking login button")

        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):

        self.logger.info("Starting login process")

        self.open_login_page()

        self.enter_email(email)

        self.enter_password(password)

        self.click_login()

        self.logger.info("Login process completed")
