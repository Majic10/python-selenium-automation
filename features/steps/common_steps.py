from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SEARCH_BOX = (By.ID, "twotabsearchtextbox")
PRODUCT_IMAGE = (By.XPATH, "//div[@data-component-type='s-search-result'][1]//img")
PRODUCT_NAME = (By.XPATH, "//div[@data-component-type='s-search-result'][1]//h2/a/span")


# Common step definitions
@given("I am on Amazon homepage")
def step_given_amazon_homepage(context):
    context.driver.get("https://www.amazon.com")


@when("I search for '{keyword}'")
def step_when_search_for(context, keyword):
    search_box = context.driver.find_element(*SEARCH_BOX)
    search_box.send_keys(keyword)
    search_box.submit()


@when('Store product name')
def step_store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when("I click on an item")
def step_when_click_on_item(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(PRODUCT_IMAGE),
        message='product not clickable'
    ).click()