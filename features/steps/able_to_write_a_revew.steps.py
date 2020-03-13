from behave import then


@then('Expected product has "write review" button')
def result_verification3(context):
    context.app.results_page.review_button_check()