import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from utilities.data_reader_util import read_csv_data,read_excel_data,read_json_data

csv_data = read_csv_data("testdata/logindata.csv")
excel_data = read_csv_data("testdata/logindata.xlsx")
json_data = read_csv_data("testdata/logindata.json")

@pytest.mark.datadriven
@pytest.mark.parametrize("testName,email,password,expected",csv_data)
def test_user_invalid_login(page,testName,email,password,expected):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()
    login_page.login(email,password)
    if expected == "success":
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)
