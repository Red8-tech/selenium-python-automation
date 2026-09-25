from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.config_reader import ConfigReader
from utilities.logger import Logger



class DriverFactory:

    @staticmethod
    def create_driver():
        config = ConfigReader()
        logger = Logger.get_logger("DriverFactory")

        browser = config.get("browser").lower()
        headless = config.get_bool("headless")

        logger.info(f"Creating browser: {browser}")

        if browser == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")

            
            driver = webdriver.Chrome(
                options=options
            )

        elif browser == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            service = FirefoxService(
                GeckoDriverManager().install()
            )

            driver = webdriver.Firefox(
                service=service,
                options=options
            )

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )


        logger.info(f"{browser} browser started successfully")
        
        driver.implicitly_wait(
            config.get_int("implicit_wait")
        )

        return driver
