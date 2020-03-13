from behave import when, then
from time import sleep


@when('Fill data from prev step')
def sign_in_fill(context):
    context.app.main_page.sign_in_button_click()
    context.app.registration_page.registration_form_email('seniorus_pomidorus1@korolevstvo.nyc')
    context.app.registration_page.registration_form_password('Zxcvb!234')


@when('Click sign_in button')
def sing_in_click(context):
    context.app.registration_page.sign_in_click()


@then('Expected login will be complete successfully')
def successful_sign_in(context):
    context.app.registration_page.sign_in_result('Welcome')
