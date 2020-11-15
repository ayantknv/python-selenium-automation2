from behave import when, then
from selenium.webdriver.common.by import By

BEST_SELLERS_BUTTON = (By. CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
BEST_SELLERS_LINKS_ONPAGE = (By. XPATH, "//div[@id='zg_tabs']")

@when ('Click on best sellers menu')
def click_on_menu(context):
    context.driver.find_element(*BEST_SELLERS_BUTTON).click()

@then ('Verify {expected_links} links on the page')
def verify_link(context, expected_links):
    result = len(context.driver.find_elements(*BEST_SELLERS_LINKS_ONPAGE))
    assert result == int(expected_links), f'Amount of links incorrect. Expected {expected_links} but got {result}'



