from pages.base_page import Page
from selenium.webdriver.common.by import By

class HamburgerMenu(Page):
    AMAZON_MUSIC_MENU = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_amazon_music(self):
        self.click(*self.AMAZON_MUSIC_MENU)

    def verify_amount_of_items(self, item_count: int):
        self.driver.wait.until(
            lambda driver: len(driver.find_elements(*self.AMAZON_MUSIC_MENU_RESULTS)) == item_count,
            f'Amount of items did not match expected {item_count}'
        )
