from utilities.csv_reader import CSVReader
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_valid_login(driver):

    data = CSVReader.read_data()[0]

    email = data["username"]
    password = data["password"]

    home_page = HomePage(driver)

    home_page.open_home_page()

    login_page = LoginPage(driver)

    login_page.login(
        email,
        password
    )

    assert home_page.is_logged_in()
