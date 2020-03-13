from behave import when, then
from time import sleep


@when('On search results page choose something and click it')
def choose_one_of_the_result(context):
    context.app.main_page.search_button_click()
    context.app.results_page.first_search_result_open()


@when('Add product to shopping cart')
def add_one_item_to_cart(context):
    context.app.shopping_cart.add_to_cart_for_delivery()


@then('Expected product would be in cart')
def result_verification(context):
    context.app.shopping_cart.item_in_the_cart_result('1')


# Не могу понять почему Селениум не видит popup, ни один локатор, что за хитрость?

@then('Close all pop-ups')
def popup_close(context):
    context.app.shopping_cart.twice_browser_back()
    # context.app.shopping_cart.popup_with_item_in_the_cart()
