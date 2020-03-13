from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ResultsPage(Page):
    ORIGINAL_KEYWORD_H1 = (By.CSS_SELECTOR, "h1 .original-keyword")
    FIELD_EMAIL = (By.CSS_SELECTOR, '#email')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '#password-input-field')
    FIELD_ZIPCODE = (By.CSS_SELECTOR, '#zipCode')
    FIELD_PHONE = (By.CSS_SELECTOR, '#phone')
    VERIFY_PHONE_CHECKBOX = (By.CSS_SELECTOR, '[data-automation-id="registrationVerifyPhoneCheckBox"]')
    ISPRO_CHECKBOX = (By.CSS_SELECTOR, '[data-automation-id="registrationIsProCheckBox"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[data-automation-id="registrationCreateAnAccountButton"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-automation-id="signInSignInButton"]')
    SKIP_PHONE_VERIFICATION = (By.CSS_SELECTOR, '[data-automation-id="registrationVerifyPhoneSkipForNowCreateMyAccountButton"]')
    REGISTRATION_RESULT = (By.CSS_SELECTOR, '[data-automation-id="subscriptionsHeader"]')
    SIGN_IN_RESULT = (By.CSS_SELECTOR, '#headerMyAccountTitle')
    EMPTY_CART_RESULT = (By.CSS_SELECTOR, '[data-automation-id="appEmptyShoppingCartText"]')
    FIRST_SEARCH_ITEM = (By.CSS_SELECTOR, '.js-pod')
    ADD_TO_CART_FOR_DELIVERY = (By.CSS_SELECTOR, 'div.buybelt__online-wrapper span.bttn__content')
    POPUP_ROOT = (By.CSS_SELECTOR, '#root')
    EXPECTED_ITEM_IN_THE_CART = (By.CSS_SELECTOR, '#headerCart .MyCart__itemCount')
    POPUP_CLICKABLE_CART_ITEM = (By.CSS_SELECTOR, '[data-automation-id="viewCartLink"]')
    POPUP_WITH_ITEM_IN_CART = (By.CSS_SELECTOR, '[data-automation-id="closeAddToCartOverlay"]')
    SECOND_PAGE_SEARCH_RESULT_LINK = (By.CSS_SELECTOR, '.grid .hd-pagination__link[title="2"]')
    CART_QUANTITY = (By.CSS_SELECTOR, '[data-automation-id="itemQuantityBoxQuantityInput"]')
    ANY_PLACE_CLICK_CART = (By.CSS_SELECTOR, '[data-automation-id="itemTotalPrice"]')
    REVIEW_BUTTON = (By.CSS_SELECTOR, '.write-review-content__submit__desktop__button .bttn__content')

    def verify_header_result(self, text):
        self.wait_for_element_appear(self.ORIGINAL_KEYWORD_H1)
        self.verify_elmnt_txt(text, *self.ORIGINAL_KEYWORD_H1)

    def registration_form_email(self, text_email: str):
        self.wait_for_element_appear(self.FIELD_EMAIL)
        self.input(text_email, *self.FIELD_EMAIL)

    def registration_form_password(self, text_password: str):
        self.wait_for_element_appear(self.FIELD_PASSWORD)
        self.input(text_password, *self.FIELD_PASSWORD)

    def registration_form_zipcode(self, text_zipcode: str):
        self.wait_for_element_appear(self.FIELD_ZIPCODE)
        self.input(text_zipcode, *self.FIELD_ZIPCODE)

    def registration_form_phone(self, text_phone: str):
        self.wait_for_element_appear(self.FIELD_PHONE)
        self.input(text_phone, *self.FIELD_PHONE)

    def phone_checkbox(self):
        self.click(*self.VERIFY_PHONE_CHECKBOX)

    def ispro_checkbox(self):
        self.click(*self.ISPRO_CHECKBOX)

    def registration_form_submit(self):
        self.click(*self.REGISTRATION_SUBMIT)

    def skip_verification(self):
        self.wait_for_element_appear(self.SKIP_PHONE_VERIFICATION)
        self.click(*self.SKIP_PHONE_VERIFICATION)

    def registration_result(self, text: str):
        self.wait_for_element_appear(self.REGISTRATION_RESULT)
        self.verify_elmnt_txt(text, *self.REGISTRATION_RESULT)

    def sign_in_click(self):
        self.click(*self.SIGN_IN_BUTTON)

    def sign_in_result(self, text: str):
        self.wait_for_element_appear(self.SIGN_IN_RESULT)
        self.verify_text_in(text, *self.SIGN_IN_RESULT)

    def empty_cart_result(self, text: str):
        self.wait_for_element_appear(self.EMPTY_CART_RESULT)
        self.verify_text_in(text, *self.EMPTY_CART_RESULT)

    def first_search_result_open(self):
        self.wait_for_element_click(self.FIRST_SEARCH_ITEM)
        self.click(*self.FIRST_SEARCH_ITEM)

    def add_to_cart_for_delivery(self):
        self.wait_for_element_appear(self.ADD_TO_CART_FOR_DELIVERY)
        self.click(*self.ADD_TO_CART_FOR_DELIVERY)

    def item_in_the_cart_result(self, text: str):
        sleep(4)
        # self.wait_for_element_click(self.POPUP_WITH_ITEM_IN_CART)
        # self.wait_for_element_appear(self.POPUP_WITH_ITEM_IN_CART)
        self.verify_text_in(text, *self.EXPECTED_ITEM_IN_THE_CART)

    def popup_with_item_in_the_cart(self):
        self.click(*self.POPUP_WITH_ITEM_IN_CART)

    def twice_browser_back(self):
        sleep(4)
        self.back()
        self.back()

    def second_page_first_search_result_open(self):
        self.wait_for_element_click(self.SECOND_PAGE_SEARCH_RESULT_LINK)
        self.click(*self.SECOND_PAGE_SEARCH_RESULT_LINK)
        self.wait_for_element_click(self.FIRST_SEARCH_ITEM)
        self.click(*self.FIRST_SEARCH_ITEM)

    def click_cart_button(self):
        self.wait_for_element_appear(self.EXPECTED_ITEM_IN_THE_CART)
        self.click(*self.EXPECTED_ITEM_IN_THE_CART)

    def change_quantity(self, quantity: str):
        self.wait_for_element_appear(self.CART_QUANTITY)
        self.input(quantity, *self.CART_QUANTITY)
        self.click(*self.ANY_PLACE_CLICK_CART)

    def review_button_check(self):
        self.wait_for_element_appear(self.REVIEW_BUTTON)
        self.verify_text_in('Write a review', *self.REVIEW_BUTTON)





















