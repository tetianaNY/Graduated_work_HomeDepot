from behave import then
from time import sleep


@then('Click cart button')
def result_page_cart(context):
    context.app.results_page.click_cart_button()


@then('Change quantity from 1 to 2')
def change_quantity(context):
    context.app.shopping_cart.change_quantity('2')


@then('Expected items in cart will be 2')
def result_verification2(context):
    context.app.shopping_cart.item_in_the_cart_result('2')
    sleep(2)
