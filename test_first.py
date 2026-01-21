from playwright.sync_api import Page, expect

def test_first(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("")
    page.locator("[data-test=\"password\"]").fill("")
    page.locator("[data-test=\"login-button\"]").click()
    msg = page.locator("[data-test=\"error\"]")
    expect(msg).to_contain_text("Username is required")
