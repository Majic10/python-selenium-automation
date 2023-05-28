from behave import given, when, then
from selenium.webdriver.common.by import By
from common_steps import step_given_amazon_homepage, step_when_search_for, step_store_product_name,\
    step_when_click_on_item

AVAILABLE_COLORS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@then("Verify all colors are clickable")
def step_colors_clickable(context):
    expected_colors = ['Black/White', 'Black', 'Blue/Coral Orange', 'Bright Pink/White']
    actual_colors = []

    colors = context.driver.find_elements(*AVAILABLE_COLORS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors
