from behave import given, when, then
from features.steps.add_to_cart import open_amazon
from selenium.webdriver.common.by import By


@when("Navigates to Amazon Home page")
def navigate_to_home_page(context):
    context.app.amazon_fashion_page.navigate_to_fashion_page()


@when("Hover over New Arrivals link")
def hover_new_arrivals(context):
    context.app.amazon_fashion_page.hover_new_arrivals()


@then("Verify deals are displayed")
def verify_deals_displayed(context):
    context.app.amazon_fashion_page.verify_deals_displayed()


