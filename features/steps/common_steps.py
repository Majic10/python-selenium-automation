from behave import given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

SEARCH_BOX = (By.ID, "twotabsearchtextbox")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "div[data-index='3'] img")
PRODUCT_NAME = (By.CSS_SELECTOR, "div[data-index='3'] h2")


# Common step definitions
@given("I am on Amazon homepage")
def step_given_amazon_homepage(context):
    context.app.home_page.open_home_page()


@when("I search for '{keyword}'")
def step_when_search_for(context, keyword):
    context.app.base_page.input_text(keyword, *SEARCH_BOX)


@when('Store product name')
def step_store_product_name(context):
    selected_product = context.app.base_page.find_element(*PRODUCT_NAME)
    product_name = selected_product.text
    print(f'Storing product name: {product_name}')



@when("I click on an item")
def step_when_click_on_item(context):
    context.app.base_page.wait_for_element_click(*PRODUCT_IMAGE)
