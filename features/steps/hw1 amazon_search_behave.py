from behave import given, when, then
from selenium.webdriver.common.by import By


#@given('open Amazon page')
#def open_amazon_page(context):
    #context.driver.get("https://www.amazon.com/")

@when ('Click on Returns & Orders')
def click_on_returns_and_orders(context):
    context.driver.find_element(By.ID, 'nav-orders'). click()

@then ('Sign in page opened')
def verify_sign_in_page_opened(context):
    result = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']")
    assert result

