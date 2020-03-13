from behave import given, when, then
from time import sleep


@when('Insert {request_text} in search field')
def search_product(context, request_text):
    context.app.main_page.search_product_noclick(request_text)


@when('Click search button or click enter button')
def search_button_clk(context):
    context.app.main_page.search_button_click()


@then('Expect to see the search results page. Check that title is relevant to {search_text}')
def assert_result(context, search_text):
    context.app.results_page.verify_header_result(search_text)
