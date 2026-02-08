from pages.homePage import HomePage
from playwright.sync_api import Page

class ProductPage(HomePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.products_title = page.locator(".title")
        self.product_container = page.locator(".inventory_item")
        self.click_cart_button = page.locator(".shopping_cart_link")
    
    def verify_on_product_page(self):
        return self.products_title
    
    def add_to_cart(self):
        products = self.product_container.all()
        for product in products:
            add_button = product.get_by_text("Add to cart", exact=True)
            add_button.click()
    
    def cart_count(self):
        cart_badge = self.page.locator(".shopping_cart_badge")
        return cart_badge.inner_text()
    
    def click_cart(self):
        self.click_cart_button.click()
