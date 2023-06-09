from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common_steps import step_given_amazon_homepage, step_when_search_for, step_when_click_on_item, \
    step_store_product_name, step_store_product_name


ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
SEARCH_BOX = (By.ID, "twotabsearchtextbox")
GO_TO_CART = (By.CSS_SELECTOR, "#attach-view-cart-button-form")
ACTUAL_RESULT = (By.CSS_SELECTOR, "div.a-row h1")



@when("I click on 'Add to Cart' button")
def add_to_cart(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(ADD_TO_CART_BTN)
    # ).click()
    context.app.base_page.click(*ADD_TO_CART_BTN)


@when("I click on 'Go to Cart' button")
def go_to_cart(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(GO_TO_CART)
    # ).click()
    context.app.base_page.click(*GO_TO_CART)


@then("Verify item(s) added to cart")
def verify_cart(context):
    # expected_text = "Shopping Cart"
    # actual_result = context.driver.find_element(*ACTUAL_RESULT).text
    # assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"
    context.app.base_page.verify_element_text('Shopping Cart', *ACTUAL_RESULT)