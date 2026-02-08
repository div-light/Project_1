from pages.checkoutPage import CheckoutPage
from playwright.sync_api import Page, expect
import pytest

def test_end2end(page: Page):
    cp = CheckoutPage(page)
    cp.navigate()
    cp.login("standard_user", "secret_sauce")
    cp.verify_on_product_page()
    cp.add_to_cart()
    assert cp.cart_count() == "6"
    cp.click_cart()
    cp.click_checkout()
    cp.fill_checkout_info()
    cp.verify_checkout_info()




