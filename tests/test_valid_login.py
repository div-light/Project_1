from playwright.sync_api import Page
from pages.homePage import HomePage
import pytest


@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_valid_login(page: Page, username, password):
    hp = HomePage(page)
    hp.navigate()
    hp.login(username, password)
    assert page.url == "https://www.saucedemo.com/inventory.html", f"Expected to be on inventory page, but was on {page.url}"

