from pages.base_page import Page


class HomePage(Page):

    def open_home_page(self):
        self.open_url('https://www.amazon.com/')
