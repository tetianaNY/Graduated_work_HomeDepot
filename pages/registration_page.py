from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Registration(Page):

    FIELD_EMAIL = (By.CSS_SELECTOR, '#email')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '#password-input-field')
    FIELD_ZIPCODE = (By.CSS_SELECTOR, '#zipCode')
    FIELD_PHONE = (By.CSS_SELECTOR, '#phone')
    VERIFY_PHONE_CHECKBOX = (By.CSS_SELECTOR, '[data-automation-id="registrationVerifyPhoneCheckBox"]')
    ISPRO_CHECKBOX = (By.CSS_SELECTOR, '[data-automation-id="registrationIsProCheckBox"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[data-automation-id="registrationCreateAnAccountButton"]')
    SKIP_PHONE_VERIFICATION = (By.CSS_SELECTOR, '[data-automation-id="registrationVerifyPhoneSkipForNowCreateMyAccountButton"]')
    REGISTRATION_RESULT = (By.CSS_SELECTOR, '[data-automation-id="subscriptionsHeader"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-automation-id="signInSignInButton"]')
    SIGN_IN_RESULT = (By.CSS_SELECTOR, '#headerMyAccountTitle')

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