from behave import given, when, then
from selenium.webdriver.common.by import By

ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
SEARCH_BOX = (By.ID, "twotabsearchtextbox")
GO_TO_CART = (By.CSS_SELECTOR, "#attach-view-cart-button-form")
ACTUAL_RESULT = (By.CSS_SELECTOR, "div.a-row h1")


@given("User is on Amazon hompage")
def open_amazon(context):
    context.app.base_page.open_url('https://www.amazon.com/')


@when("Search for '{search_keyword}'")
def search_amazon(context, search_keyword):
    context.app.header.search_amazon(search_keyword)


@when("Click on an item")
def click_on_item(context):
    context.app.search_results_page.click_on_item()


@when("Store product name")
def store_product_name(context):
    context.app.cart_page.store_product_name()


@when("Click on 'Add to Cart' button")
def add_to_cart(context):
    context.app.cart_page.add_to_cart()


@when("Click on 'Go to Cart' button")
def go_to_cart(context):
    context.app.cart_page.go_to_cart()


@then("Verify item(s) added to cart")
def verify_cart(context):
    context.app.cart_page.verify_cart_items()
