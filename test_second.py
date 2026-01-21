from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
     ("sdfdfa", "secret_sauce"),
    ("sdfdfa",""),
    ("",""),
    ("","secret_sauce")
])
def test_second(page: Page, username, password):
    # Pytest-Playwright opens the page for you automatically
    page.goto("https://www.saucedemo.com")

    # Fill the login form
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    if username == "locked_out_user":
        # Check for error message
        error_msg = page.locator("[data-test='error']")
        expect(error_msg).to_contain_text("Sorry, this user has been locked out.")
    
    elif username == "sdfdfa" and password == "":
        error_msg = page.locator("[data-test='error']")
        expect(error_msg).to_contain_text("Password is required")

    elif username == "" and password == "":
        error_msg = page.locator("[data-test='error']")
        expect(error_msg).to_contain_text("Username is required")

    elif username == "" and password == "secret_sauce":
        error_msg = page.locator("[data-test='error']")
        expect(error_msg).to_contain_text("Username is required")

    elif username == "sdfdfa" and password == "secret_sauce":
        error_msg = page.locator("[data-test='error']")
        expect(error_msg).to_contain_text("Username and password do not match any user in this service")


    else:
        expect(page.locator("span[class='title']")).to_have_text("Products")
        