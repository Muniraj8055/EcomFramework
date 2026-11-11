import time
import pytest
from playwright.sync_api import expect

import config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.my_account_page import MyAccountPage
from config import Config

@pytest.mark.regression
def test_user_logout(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()
    login_page.login(Config.email, Config.password)
    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
    my_account_page.click_logout()
    logout_page.click_continue()
    expect(page).to_have_title("Your Store")
