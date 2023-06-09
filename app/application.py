from pages.base_page import Page
from pages.header import Header
from pages.home_page import HomePage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.home_page = HomePage(self.driver)
        self.base_page = Page(self.driver)