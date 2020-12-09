from behave import given, then
from selenium.webdriver.common.by import By


@when('Click on hamburger menu')
def click_on_ham_menu(context):
    context.app.main_page.click_hamburger_menu()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.hamburger_menu.click_amazon_music()

@then('{item_count} menu items are present')
def verify_items_present(context, item_count):
    context.app.hamburger_menu.verify_amount_of_items(int(item_count))
