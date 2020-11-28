from behave import given, then
from selenium.webdriver.common.by import By

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')

@given ('Open amazon best sellers')
def open_page(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs')

@then ('Click on each top link and verify new page opens')
def click_through(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link.text
        link.click()
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f"Expected {link_text} not in {header_text}"




