from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_basket(self):
        self.page.click("input#add-to-cart-button")

    def navigate_to_basket(self):
        self.page.click("a#nav-cart")
