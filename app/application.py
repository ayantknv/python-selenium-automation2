from pages.main_page import MainPage
from pages.signin_page import sign_in_page
from pages.hamburger_menu import HamburgerMenu

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.signin_page = sign_in_page(self.driver)
        self.hamburger_menu = HamburgerMenu(self.driver)





