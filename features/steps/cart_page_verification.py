from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given("User is on Amazon homepage")
# def open_amazon(context):
#     context.driver.get("https://www.amazon.com")


@when("User navigates to the cart page")
def open_cart_page(context):
    context.driver.find_element(By.ID, "nav-cart").click()


@then("Cart page is displayed with no items in it")
def verify_cart(context):
    expected_text = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty").text
    assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"
    sleep(4)