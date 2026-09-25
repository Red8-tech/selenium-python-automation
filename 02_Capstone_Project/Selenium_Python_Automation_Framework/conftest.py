import pytest
import allure

from utilities.driver_factory import DriverFactory
from utilities.screenshot import Screenshot
from utilities.logger import Logger


@pytest.fixture
def driver():
    driver = DriverFactory.create_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            try:

                screenshot_path = Screenshot.take_screenshot(
                    driver,
                    item.name
                )

                with open(
                    screenshot_path,
                    "rb"
                ) as image_file:

                    allure.attach(
                        image_file.read(),
                        name=item.name,
                        attachment_type=allure.attachment_type.PNG
                    )

            except Exception as e:

                logger = Logger.get_logger(
                    "Screenshot"
                )

                logger.error(
                    f"Could not capture screenshot: {e}"
                )
