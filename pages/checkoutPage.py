from pages.productPage import ProductPage
from playwright.sync_api import Page


class CheckoutPage(ProductPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")


    def click_checkout(self):
        self.checkout_button.click()
    
    def fill_checkout_info(self):
        self.first_name_input.fill("User")
        self.last_name_input.fill("Second")
        self.postal_code_input.fill("123456")
        self.continue_button.click()
        self.finish_button.click()
    
    def verify_checkout_info(self):
        return self.page.screenshot(path="screenshots/checkout_info.png")
    
    
    


    


