from behave import given, when, then
from time import sleep


@given('Open HomeDepot page')
def open_homedepot_page(context):
    context.app.main_page.open_p()


@when('Enter {search_word} to the search box')
def search_input(context, search_word):
    context.app.main_page.search_product_noclick(search_word)
    context.app.main_page.search_field_click()
    sleep(3)


@then('Count {search_word} on the page')
def count_input(context, search_word):
    context.app.main_page.counting_result(search_word)