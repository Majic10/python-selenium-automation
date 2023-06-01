from common_steps import step_given_amazon_homepage
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TERMS_CONDITIONS_PAGE = (
    By.CSS_SELECTOR, "a.nav_a[href='/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou']")
PRIVACY_LINK = (By.CSS_SELECTOR, "a.help-display-cond[href='https://www.amazon.com/privacy']")


@given("User is on the Amazon Terms and Conditions page")
def step_open_amazon_terms_conditions_page(context):
    terms_conditions_page = context.driver.find_element(*TERMS_CONDITIONS_PAGE)
    terms_conditions_page.click()


@given("Store the current window")
def step_store_current_window(context):
    context.original_window = context.driver.current_window_handle


@when("User opens the Amazon Privacy Notice link")
def step_open_amazon_privacy_page(context):
    privacy_link = context.driver.find_element(*PRIVACY_LINK)
    privacy_link.click()


@when("Switch to the newly opened window")
def step_switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then("User verifies that the Amazon Privacy Notice page is opened")
def step_verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('www.amazon.com/gp/help/customer/'))


@then("Close the new window")
def step_close_new_window(context):
    context.driver.close()


@then("Switch back to the original window")
def step_switch_back(context):
    context.driver.switch_to.window(context.original_window)