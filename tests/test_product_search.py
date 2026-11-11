import time
import pytest
from playwright.sync_api import expect

from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
from config import Config  # Configuration file holding credentials
from pages.product_page import ProductPage

@pytest.mark.sanity
@pytest.mark.regression
def test_search_product(page):
    product = Config.product_name
    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    home_page.enter_product_name(product)
    home_page.click_search()
    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)
    expect(search_results_page.is_product_exist(product)).to_be_visible(timeout=3000)