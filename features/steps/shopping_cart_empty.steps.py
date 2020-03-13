from behave import when, then
from time import sleep


@when('Click HomeDepot cart button')
def cart_button(context):
    context.app.main_page.cart_button_click()


@then('Expected cart page will have {empty_text} in the title')
def empty_cart(context, empty_text):
    context.app.shopping_cart.empty_cart_result(empty_text)
