import unittest

from utilities.driver_factory import DriverFactory
from pages.home_page import HomePage


class TestHomePage(unittest.TestCase):

    def setUp(self):

        self.driver = DriverFactory.create_driver()

        self.home_page = HomePage(
            self.driver
        )

    def tearDown(self):

        if self.driver:
            self.driver.quit()

    def test_home_page_displayed(self):

        self.home_page.open_home_page()

        assert self.home_page.is_home_page_displayed()


if __name__ == "__main__":
    unittest.main()
