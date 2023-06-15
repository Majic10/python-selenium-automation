from pages.base_page import Page
from pages.header import Header
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.signin_page import SigninPage
from pages.search_results_page import SearchResultsPage
from pages.amazon_fashion_page import AmazonFashionPage
from pages.amazon_departments import AmazonDepartmentsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.home_page = HomePage(self.driver)
        self.base_page = Page(self.driver)
        self.cart_page = CartPage(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.amazon_fashion_page = AmazonFashionPage(self.driver)
        self.amazon_departments = AmazonDepartmentsPage(self.driver)
