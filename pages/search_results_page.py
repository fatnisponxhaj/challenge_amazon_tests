from playwright.sync_api import Page

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def select_first_product(self):
        self.page.click("div.s-main-slot div.s-result-item h2 a")
