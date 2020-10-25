from behave import when, then
from selenium.webdriver.common.by import By
from selenium import webdriver

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
FACE_MASK_RESULT = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
SEARCH_BUTTON = (By.CSS_SELECTOR, "input.nav-input[value=Go]")

@when ('In the search field input face mask')
def input_search(context):
    input_field = context.driver.find_element(*SEARCH_INPUT)
    input_field.send_keys('face mask')
    context.driver.find_element(*SEARCH_BUTTON).click()

@then ('Verify face mask inquiry is shown')
def verify_mug(context):
    result = context.driver.find_element(*FACE_MASK_RESULT)
    assert "face mask" in result.text


FACE_MASK = (By.XPATH, "//div[@data-component-type='s-impression-logger']//img[@data-image-latency='s-product-image']")
ADD_TO_CART = (By.CSS_SELECTOR, "input#add-to-cart-button")
PRODUCT_IN_THE_CART = (By.ID,"huc-v2-order-row-with-divider")


@when ('Input face mask on the search field')
def input_search(context):
    input_field = context.driver.find_element(*SEARCH_INPUT)
    input_field.send_keys('face mask')
    context.driver.find_element(*SEARCH_BUTTON).click()


@when ('Select second product on the list')
def select_product(context):
    context.driver.find_element(*FACE_MASK).click()


@when ('Add the product to the shopping cart')
def click_add_to_card (context):
    context.driver.find_element(*ADD_TO_CART).click()


@then ('Verify selected product on shopping cart')
def verify_product(context):
    result = context.driver.find_element(*PRODUCT_IN_THE_CART)
    assert result
