import pytest
from pages.amazon_homepage import AmazonHomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

@pytest.mark.parametrize("product_name, quantity", [("Dell Precision 5000 5570", 2)])
def test_amazon_shopping(page, product_name, quantity):
    home_page = AmazonHomePage(page)
    search_results_page = SearchResultsPage(page)
    product_page = ProductPage(page)
    basket_page = BasketPage(page)

    # Step 1: Load the Amazon homepage
    print("Loading Amazon homepage")
    home_page.load()
    page.screenshot(path="screenshots/step1_homepage_loaded.png")

    # Step 2: Search for a product
    print(f"Searching for product: {product_name}")
    home_page.search_product(product_name)
    page.screenshot(path="screenshots/step2_search_results.png")

    # Step 3: Select the first product from search results
    print("Selecting the first product from search results")
    search_results_page.select_first_product()
    page.screenshot(path="screenshots/step3_product_page.png")

    # Step 4: Add the product to the basket
    print("Adding the product to the basket")
    product_page.add_to_basket()
    page.screenshot(path="screenshots/step4_added_to_basket.png")

    # Step 5: Navigate to the basket
    print("Navigating to the basket")
    product_page.navigate_to_basket()
    page.screenshot(path="screenshots/step5_basket_page.png")

    # Step 6: Update the quantity of the product in the basket
    print(f"Updating the quantity to: {quantity}")
    basket_page.update_quantity(quantity)
    page.screenshot(path="screenshots/step6_quantity_updated.png")

    # Step 7: Assert the quantity of the product in the basket
    current_quantity = basket_page.get_quantity()
    print(f"Current quantity in the basket: {current_quantity}")
    
    assert current_quantity == str(quantity)
