from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common_steps import step_given_amazon_homepage, step_when_search_for, step_when_click_on_item, \
    step_store_product_name

PRODUCT = (By.CSS_SELECTOR, "img.s-image[src='https://m.media-amazon.com/images/I/81HTgYFwyfL._AC_UL400_.jpg']")
ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
SEARCH_BOX = (By.ID, "twotabsearchtextbox")
GO_TO_CART = (By.CSS_SELECTOR, "a[href='/cart?ref_=sw_gtc']")
ACTUAL_RESULT = (By.CSS_SELECTOR, "div.a-row h1")



@when("I click on 'Add to Cart' button")
def add_to_cart(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN)
    ).click()


@when("I click on 'Go to Cart' button")
def go_to_cart(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(GO_TO_CART)
    ).click()


@then("Verify item(s) added to cart")
def verify_cart(context):
    expected_text = "Shopping Cart"
    actual_result = context.driver.find_element(*ACTUAL_RESULT).text
    assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"