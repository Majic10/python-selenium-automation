from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SigninPage(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def verify_signin_opens(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        self.verify_element_text('Sign in', *self.SIGNIN_TEXT)






