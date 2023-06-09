from selenium.webdriver.common.by import By
from behave import given, when, then


ORDERS_PAGE = (By.ID, "nav-orders")
SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


@given("User is on Amazon homepage")
def open_amazon(context):
    context.app.home_page.open_home_page()


@when("User navigates to signin page")
def open_orders_page(context):
    context.app.base_page.click(*ORDERS_PAGE)


@then("The sign-in page is displayed")
def verify_signin(context):
    context.app.base_page.verify_partial_text('Sign in', *SIGNIN_TEXT)