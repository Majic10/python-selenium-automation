from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class CartPage(Page):
    CART_MESSAGE = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    GO_TO_CART = (By.CSS_SELECTOR, "#attach-view-cart-button-form")
    CHECKOUT_BTN = (By.ID, "sc-buy-box-ptc-button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[data-index='3'] h2")


    def verify_cart_empty(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/cart'))
        self.verify_element_text('Your Amazon Cart is empty', *self.CART_MESSAGE)

    def add_to_cart(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()


    def go_to_cart(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.GO_TO_CART)).click()


    def verify_cart_items(self):
        self.wait_for_element_appear(*self.CHECKOUT_BTN)

    def store_product_name(self):
        selected_product = self.driver.find_element(*self.PRODUCT_NAME)
        product_name = selected_product.text
        return product_name


