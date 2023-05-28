from email.mime import image

from behave import given, when, then
from selenium.webdriver.common.by import By
from common_steps import step_given_amazon_homepage, step_when_search_for

PRODUCT_IMAGE = (By.XPATH, "//div[@data-component-type='s-search-result']//img")
PRODUCT_NAME = (By.XPATH, "//div[@data-component-type='s-search-result']//h2/a/span")
PRODUCTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")


@then("verify products have picture and name")
def step_verify_products(context):
    products = context.driver.find_elements(*PRODUCTS)
    verification_results = []

    for product in products:
        product_name = product.find_element(*PRODUCT_NAME)
        product_image = product.find_element(*PRODUCT_IMAGE)

        result = {
            'product_name': product_name.text,
            'has_image': product_image.is_displayed(),
            'has_name': product_name.text != ""
        }

        verification_results.append(result)

        assert result['has_image']
        assert result['has_name']

    context.verification_results = verification_results


@then("Print verification results")
def step_print_verification_results(context):
    for result in context.verification_results:
        product_name = result['product_name']
        has_image = result['has_image']
        has_name = result['has_name']

        print(f"Product Name: {product_name}")
        print(f"Has Image: {has_image}")
        print(f"Has Name: {has_name}")

