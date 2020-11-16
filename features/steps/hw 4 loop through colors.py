from behave import given, then
from selenium.webdriver.common.by import By

color_option = (By.CSS_SELECTOR, "#variation_color_name li")
selected_color = (By.CSS_SELECTOR, "#variation_color_name span.selection")


@given('Open Amazon Jeans {productid} page')
def open_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can select through colors')
def verify_items(context):
    #expected_colors = ['Black', 'Blue overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash']
    colors = context.driver.find_elements(*color_option)

    for color in colors:
        color.click()
        assert context.driver.find_element(*selected_color).text != ''




