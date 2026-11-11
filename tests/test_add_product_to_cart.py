import time
import pytest
from playwright.sync_api import expect

import config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.my_account_page import MyAccountPage
from config import Config
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage


@pytest.mark.regression
def test_add_product_to_cart(page):

    product_name = Config.product_name
    product_quantity = Config.product_quantity

    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()
    product_page = search_results_page.select_product(product_name)
    product_page.set_quantity(product_quantity)
    product_page.add_to_cart()

    expect(product_page.get_confirmation_message()).to_be_visible(timeout=3000)
