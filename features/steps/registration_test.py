from behave import when, then
from time import sleep


@when('Click account button')
def click_account(context):
    context.app.main_page.account_button_click()


@when('Click "register" button')
def click_register(context):
    context.app.main_page.register_button_click()


# Prior to run the test change e-mail (just add 1 to the name) and phone number (change 1 digit)
@when('Fill all fields with fake data')
def registration_form(context):
    context.app.registration_page.registration_form_email('seniorus_pomidorus655@korolevstvo.nyc')
    context.app.registration_page.registration_form_password('Zxcvb!234')
    context.app.registration_page.registration_form_zipcode('07093')
    context.app.registration_page.registration_form_phone('2015636565')
    context.app.registration_page.phone_checkbox()
    # context.app.results_page.ispro_checkbox()


@when('Click submit registration form')
def click_submit_registration(context):
    context.app.registration_page.registration_form_submit()
    context.app.registration_page.skip_verification()


@then('Expected registration will be complete successfully')
def reg_result(context):
    context.app.registration_page.registration_result("You're Registered!")
    sleep(2)
