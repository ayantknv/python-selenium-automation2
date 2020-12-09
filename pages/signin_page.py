from pages.base_page import Page
from selenium.webdriver.common.by import By

class sign_in_page(Page):
    SIGNIN_PAGE = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_signin_page(self, expected_text: str):
        self.verify_text(expected_text, *self.SIGNIN_PAGE)


