from behave import when, then
from selenium.webdriver.common.by import By

items = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div:nth-of-type(6) li")
PRODUCT = (By.XPATH, "//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")



@given('Open Amazon product {productid} page')
def open_page(context, productid):
    context.driver.get(f'https://www.amazon.com/{productid}/')

@then ('Verify items and product name')
def verify_items(context):
    all_items = context.driver.find_elements(*items)
    for item in all_items:
        assert "Regular" or "Hundreds more in store. Look for the yellow signs" in item.text, f"expected 'Regular' to be in {item.text}"
        assert item.find_element(*PRODUCT)

