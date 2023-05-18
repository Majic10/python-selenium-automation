from selenium.webdriver.common.by import By
from behave import when, then

CUSTOMER_SERVICE_LINK = (By.CSS_SELECTOR, "a[href*='customerservice']")
H1_HEADER = (By.XPATH, "//h1[text()='Welcome to Amazon Customer Service']")
SERVICES = (By.CSS_SELECTOR, ".issue-card-container")
H2_HEADER = (By.XPATH, "//h2[text()='Search our help library']")
SEARCH_FIELD = (By.ID, "hubHelpSearchInput")
H2_ALL_TOPICS = (By.XPATH, "//h2[text()='All help topics']")
TOPICS_LIST = (By.CSS_SELECTOR, "div.help-topics-list-wrapper")


@when("User navigates to customer service page")
def open_customer_service_page(context):
    context.driver.find_element(*CUSTOMER_SERVICE_LINK).click()


@then("the 'Welcome to Amazon Customer Service' section is displayed")
def verify_welcome_section(context):
    assert context.driver.find_element(*H1_HEADER)
    assert context.driver.find_element(*SERVICES)


@then("User should see a help section")
def verify_help_section(context):
    assert context.driver.find_element(*H2_HEADER)
    assert context.driver.find_element(*SEARCH_FIELD)
    assert context.driver.find_element(*H2_ALL_TOPICS)
    assert context.driver.find_element(*TOPICS_LIST)