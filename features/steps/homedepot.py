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

@when('Insert {request_text} in search field')
def search_product(context, request_text):
    context.app.main_page.search_product_noclick(request_text)

@when('Click search button or click enter button')
def search_button_clk(context):
    context.app.main_page.search_button_click()

@then('Expect to see the search results page. Check that title is relevant to {search_text}')
def assert_result(context, search_text):
    context.app.results_page.verify_header_result(search_text)

@when('Click account button')
def click_account(context):
    context.app.main_page.account_button_click()

@when('Click "register" button')
def click_register(context):
    context.app.main_page.register_button_click()

# Prior to run the test change e-mail (just add 1 to the name) and phone number (change 1 digit)
@when('Fill all fields with fake data')
def registration_form(context):
    context.app.results_page.registration_form_email('seniorus_pomidorus674@korolevstvo.nyc')
    context.app.results_page.registration_form_password('Zxcvb!234')
    context.app.results_page.registration_form_zipcode('07093')
    context.app.results_page.registration_form_phone('2015676565')
    context.app.results_page.phone_checkbox()
    # context.app.results_page.ispro_checkbox()

@when('Click submit registration form')
def click_submit_registration(context):
    context.app.results_page.registration_form_submit()
    context.app.results_page.skip_verification()

@then('Expected registration will be complete successfully')
def reg_result(context):
    context.app.results_page.registration_result("You're Registered!")
    sleep(2)

@when('Fill data from prev step')
def sign_in_fill(context):
    context.app.main_page.sign_in_button_click()
    context.app.results_page.registration_form_email('seniorus_pomidorus1@korolevstvo.nyc')
    context.app.results_page.registration_form_password('Zxcvb!234')

@when('Click sign_in button')
def sing_in_click(context):
    context.app.results_page.sign_in_click()

@then('Expected login will be complete successfully')
def successful_sign_in(context):
    context.app.results_page.sign_in_result('Welcome')

@when('Click HomeDepot cart button')
def cart_button(context):
    context.app.main_page.cart_button_click()

@then('Expected cart page will have {empty_text} in the title')
def empty_cart(context, empty_text):
    context.app.results_page.empty_cart_result(empty_text)

@when('On search results page choose something and click it')
def choose_one_of_the_result(context):
    context.app.main_page.search_button_click()
    context.app.results_page.first_search_result_open()

@when('Add product to shopping cart')
def add_one_item_to_cart(context):
    context.app.results_page.add_to_cart_for_delivery()

@then('Expected product would be in cart')
def result_verification(context):
    context.app.results_page.item_in_the_cart_result('1')

# Не могу понять почему Селениум не видит popup, ни один локатор, что за хитрость?

@then('Close all pop-ups')
def popup_close(context):
    context.app.results_page.twice_browser_back()
    # context.app.results_page.popup_with_item_in_the_cart()


@when('Return to product search page')
def twice_back(context):
    context.app.results_page.twice_browser_back()

@when('On search results page choose another product and click it')
def new_search_result(context):
    context.app.results_page.first_search_result_open()
    # context.app.results_page.second_page_first_search_result_open()

@then('Expected products would be in cart')
def second_result_verification(context):
    context.app.results_page.item_in_the_cart_result('2')

@then('Click cart button')
def result_page_cart(context):
    context.app.results_page.click_cart_button()

@then('Change quantity from 1 to 2')
def change_quantity(context):
    context.app.results_page.change_quantity('2')

@then('Expected items in cart will be 2')
def result_verification2(context):
    context.app.results_page.item_in_the_cart_result('2')
    sleep(2)

@then('Expected product has "write review" button')
def result_verification3(context):
    context.app.results_page.review_button_check()

















