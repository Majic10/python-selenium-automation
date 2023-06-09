from selenium.webdriver.common.by import By
from behave import when, then


CART_ICON = (By.ID, "nav-cart")
CART_MESSAGE = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")


@when("User navigates to the cart page")
def open_cart_page(context):
    context.app.base_page.click(*CART_ICON)


@then("Cart page is displayed with no items in it")
def verify_cart(context):
    context.app.base_page.verify_element_text('Your Amazon Cart is empty', *CART_MESSAGE)