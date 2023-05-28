from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("User is on Amazon homepage")
def open_amazon(context):
    context.driver.get("https://www.amazon.com")


@when("User navigates to the orders page")
def open_orders_page(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@then("The sign-in page is displayed")
def verify_signin(context):
    expected_text = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"
    assert context.driver.find_element(By.ID, "ap_email")