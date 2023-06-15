from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.ID, "nav-cart")
    ORDERS_PAGE = (By.ID, "nav-orders")
    LANGUAGE_OPTIONS = (By.ID, "icp-nav-flyout")
    SPANISH_LANGUAGE = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECTION = (By.ID, "searchDropdownBox")

    def search_amazon(self, search_keyword):
        self.input_text(search_keyword, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_PAGE)


    def select_computers_department(self):
        department_selection = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_selection)
        select.select_by_value('search-alias=computers')
