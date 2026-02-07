from playwright.sync_api import sync_playwright
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chromium",
                     help="Browser selection to run tests")
    
    parser.addoption("--mobile",
                     action="store_true",
                     help="Run tests in mobile emulation mode")
    
@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name not in ["chromium", "firefox", "webkit"]:
        raise ValueError(f"Unsupported browser: {browser_name}. Choose from 'chromium', 'firefox', or 'webkit'.")
    
    playwright = sync_playwright().start()

    if browser_name == "chromium":
        browser_instance= playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser_instance = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser_instance = playwright.webkit.launch(headless=False)

    yield browser_instance
    browser_instance.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser, request):
    is_mobile = request.config.getoption("--mobile")
    if is_mobile:
        context = browser.new_context(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1"
        )
    else:
        context = browser.new_context()

    page = context.new_page()
    yield page
    page.close()
    context.close()
