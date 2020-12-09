from selenium.webdriver.support.wait import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text: str, *locator):
       actual_text = self.driver.find_element(*locator).text
       assert expected_text == actual_text, f'Expected {expected_text} does not match {actual_text}'








