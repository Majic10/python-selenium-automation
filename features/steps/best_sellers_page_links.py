from selenium.webdriver.support.wait import WebDriverWait
from common_steps import step_given_amazon_homepage
from best_sellers_page import open_bestsellers_page
from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


TARGETED_LINKS = (By.CSS_SELECTOR, "#zg_header ul li a")


@then("User verifies all links are clickable and open")
def step_click_on_all_links(context):
    expected_links = ["Best Sellers", "New Releases", "Movers & Shakers", "Most Wished For", "Gift Ideas"]
    link_texts = []

    for link_index in range(len(expected_links)):
        all_links = context.driver.find_elements(*TARGETED_LINKS)
        link = all_links[link_index]
        link_text = link.text
        link_texts.append(link_text)
        WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(link))
        link.click()

    print("Expected Links:", expected_links)
    print("Actual Links:", link_texts)

    assert expected_links == link_texts
