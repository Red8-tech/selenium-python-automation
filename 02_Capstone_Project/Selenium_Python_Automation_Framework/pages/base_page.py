from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.config = ConfigReader()

        self.wait = WebDriverWait(
            self.driver,
            self.config.get_int("explicit_wait")
        )

    def open_url(self, url):
        self.driver.get(url)

        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
