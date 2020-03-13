from behave import given, when, then


@when('Return to product search page')
def twice_back(context):
    context.app.shopping_cart.twice_browser_back()


@when('On search results page choose another product and click it')
def new_search_result(context):
    context.app.results_page.first_search_result_open()
    # context.app.shopping_cart.second_page_first_search_result_open()


@then('Expected products would be in cart')
def second_result_verification(context):
    context.app.shopping_cart.item_in_the_cart_result('2')
