from utilities.csv_reader import CSVReader
from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_product_search(driver):

    data = CSVReader.read_data()[0]

    product = data["product"]

    home_page = HomePage(driver)

    home_page.open_home_page()

    assert home_page.is_home_page_displayed()

    search_page = SearchPage(driver)

    search_page.search_product(product)

    assert search_page.is_search_results_displayed()

    products = search_page.get_product_names()

    assert any(
        product.lower() in name.lower()
        for name in products
    )
