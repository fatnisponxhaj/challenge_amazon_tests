import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # args=["--start-maximized"]
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport=None)  # viewport=None uses full screen dimensions        
    page = context.new_page()
    yield page
    context.close()
