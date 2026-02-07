from playwright.sync_api import Page, expect
from pages.homePage import HomePage
import pytest


@pytest.mark.parametrize("username, password", [
    ("locked_out_user", "secret_sauce"),
    ("", "secret_sauce"),
    ("standard_user", ""),
])
def test_valid_login(page: Page, username, password):
    hp = HomePage(page)
    hp.navigate()
    hp.login(username, password)
    error_message = page.locator("h3[data-test='error']")
    expect(error_message).to_be_visible()
    