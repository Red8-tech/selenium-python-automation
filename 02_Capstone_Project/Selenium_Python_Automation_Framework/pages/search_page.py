from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import Logger


class SearchPage(BasePage):

    SEARCH_INPUT = (
        By.NAME,
        "search"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn.btn-default.btn-lg"
    )

    SEARCH_RESULTS_TITLE = (
        By.XPATH,
        "//h1[contains(normalize-space(), 'Search')]"
    )

    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        ".product-thumb h4 a"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger("SearchPage")

    def open_products_page(self):
        self.logger.info("Waiting for search page")

        self.find_element(
            self.SEARCH_INPUT
        )

    def search_product(self, product_name):

        self.logger.info(
            f"Searching for product: {product_name}"
        )

        self.enter_text(
            self.SEARCH_INPUT,
            product_name
        )

        self.click(
            self.SEARCH_BUTTON
        )

    def is_search_results_displayed(self):

        self.logger.info(
            "Verifying search results are displayed"
        )

        return self.find_element(
            self.SEARCH_RESULTS_TITLE
        ).is_displayed()

    def get_product_names(self):

        self.logger.info(
            "Getting product names from search results"
        )

        elements = self.driver.find_elements(
            *self.PRODUCT_NAMES
        )

        return [
            element.text
            for element in elements
        ]
