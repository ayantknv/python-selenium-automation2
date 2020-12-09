from behave import given, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_amazon()

@when('Click Amazon Orders link')
def click_orders_btn(context):
    context.app.main_page.click_orders_btn()

@then('Verify Sign In page is opened')
def verify_signin_page(context):
    context.app.signin_page.verify_signin_page("Sign-In")


