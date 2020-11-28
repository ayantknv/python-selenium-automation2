from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

signin_btn = (By.CSS_SELECTOR, '#nav-signin-tooltip span')



@when ('Sign in popup is present')
def check_popup(context):
    context.driver.wait.until(EC.presence_of_all_elements_located(signin_btn))
    context.driver.wait.until(EC.element_to_be_clickable(signin_btn))

@when ('Sign in popup disappears')
def popup_disap(context):
    context.driver.wait.until(EC.invisibility_of_element(signin_btn))

@then('Verify Sign-in popup is not visible')
def verify_signin(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(signin_btn))
