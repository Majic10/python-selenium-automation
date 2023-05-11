from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given("I am on the Amazon homepage")
def open_amazon(context):
    context.driver.get("https://www.amazon.com")

@when("I search for 'Pen'")
def amazon_search(context):
    # perform a search for a product
    search_box = context.driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Pen")
    search_box.submit()
    time.sleep(4)

@when("I click on an item")
def select_item(context):
    # select the desired product and add it to cart
    product = context.driver.find_element(By.CSS_SELECTOR, "img.s-image[src='https://m.media-amazon.com/images/I/81HTgYFwyfL._AC_UL400_.jpg']")
    time.sleep(4)
    context.driver.execute_script("arguments[0].scrollIntoView();", product)
    product.click()
    time.sleep(4)

@when("I click on 'Add to Cart' button")
def add_to_cart(context):
    add_to_cart_btn = context.driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart_btn.click()
    time.sleep(4)

@when("I click on 'Go to Cart' button")
def go_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart?ref_=sw_gtc']").click()

@then("Verify item(s) added to cart")
def verify_cart(context):
    expected_text = "Shopping Cart"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row h1").text
    assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"

    time.sleep(10)
    context.driver.quit()