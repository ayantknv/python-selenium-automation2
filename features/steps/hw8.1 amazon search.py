from behave import given, then

@when('Select electronics department')
def select_electronics_department(context):
    context.app.main_page.select_electronics_department()

@then ('Search for {search_word}')
def input_search(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).sent_keys(search_word)

@when (Click_)






