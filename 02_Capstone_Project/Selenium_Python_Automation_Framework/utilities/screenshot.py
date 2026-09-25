from pathlib import Path
from datetime import datetime


class Screenshot:

    @staticmethod
    def take_screenshot(driver, test_name):

        project_root = Path(__file__).resolve().parents[1]

        screenshot_directory = project_root / "screenshots"
        screenshot_directory.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = f"{test_name}_{timestamp}.png"

        screenshot_path = screenshot_directory / file_name

        driver.save_screenshot(str(screenshot_path))

        return screenshot_path
