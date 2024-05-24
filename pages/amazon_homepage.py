from playwright.sync_api import Page

class AmazonHomePage:
    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto("https://www.amazon.com")
        self.page.wait_for_selector("input#twotabsearchtextbox")

    def search_product(self, product_name: str):
        self.page.fill("input#twotabsearchtextbox", product_name)
        self.page.click("input#nav-search-submit-button")
        self.page.wait_for_selector("div.s-main-slot")  # Ensure search results are loaded
