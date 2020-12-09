from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    RETURNS_AND_ORDERS_BTN = (By.CSS_SELECTOR, "#nav-orders")
    HAMBURGER_MENU = (By.CSS_SELECTOR, "i.hm-icon.nav-sprite")

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def click_orders_btn(self):
        self.click(*self.RETURNS_AND_ORDERS_BTN)

    def click_hamburger_menu(self):
        self.click(*self.HAMBURGER_MENU)








