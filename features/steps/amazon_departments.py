from behave import given, when, then
from selenium.webdriver.common.by import By
from features.steps.add_to_cart import open_amazon, search_amazon


@when("Select computers department")
def select_computers_department(context):
    context.app.header.select_computers_department()


@then("Verify the correct department is displayed")
def verify_department(context):
    context.app.amazon_departments.verify_department()
