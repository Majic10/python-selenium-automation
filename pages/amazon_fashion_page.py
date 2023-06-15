from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page


class AmazonFashionPage(Page):
    AMAZON_FASHION_LINK = (By.CSS_SELECTOR, "a[href='/amazon-fashion/b/?ie=UTF8&node=7141123011&ref_=nav_cs_fashion']")
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    DEALS = (By.ID, "nav-flyout-anchor")

    def navigate_to_fashion_page(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.AMAZON_FASHION_LINK)).click()

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)

        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_deals_displayed(self):
        self.wait_for_element_appear(*self.DEALS)
