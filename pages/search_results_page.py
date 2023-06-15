from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SearchResultsPage(Page):
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "div[data-index='3'] img")

    def click_on_item(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.PRODUCT_IMAGE)).click()
