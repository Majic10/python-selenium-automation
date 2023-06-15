from pages.base_page import Page
from selenium.webdriver.common.by import By


class AmazonDepartmentsPage(Page):
    COMPUTERS_SUBMENU = (By.CSS_SELECTOR, "[aria-label='Computers']")

    def verify_department(self):
        self.wait_for_element_appear(*self.COMPUTERS_SUBMENU)
