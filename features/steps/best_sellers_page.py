from selenium.webdriver.common.by import By
from behave import when, then

BEST_SELLERS_LINK = (By.CSS_SELECTOR, "#nav-xshop a[href*='bestsellers']")
BEST_SELLERS_PAGE_LINKS = (By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")
CLICKED_LINK = (By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP")


@when("User navigates to best sellers page")
def open_bestsellers_page(context):
    context.driver.find_element(*BEST_SELLERS_LINK).click()


@then("Clicked link is displayed")
def verify_clicked_link(context):
    print(context.driver.find_element(*CLICKED_LINK), "This is the clicked link in Best Sellers Page")
    assert context.driver.find_element(*CLICKED_LINK)


@then("{expected_number} links should be displayed on the page")
def verify_4links(context, expected_number):
    expected_number = int(expected_number)
    links_counter = len(context.driver.find_elements(*BEST_SELLERS_PAGE_LINKS))
    print(context.driver.find_elements(*BEST_SELLERS_PAGE_LINKS),
          "Here are 4 links besides the clicked link in Best Sellers Page")
    assert links_counter == expected_number, f"Expected 4 links but got {expected_number} links"
