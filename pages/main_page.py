from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SEARCH_BOX_LOCATOR = (By.CSS_SELECTOR, '#headerSearch')
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#headerSearchButton')
    ACCOUNT_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#headerMyAccount')
    REGISTER_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#SPSORegister a.bttn-outline .bttn__content')
    SIGN_IN_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#SPSOSignIn a.bttn--primary .bttn__content')
    SUGGESTIONS_CONTAINER = (By.CSS_SELECTOR, '#typeAheadFlyOut a')
    SUGGESTIONS_LOCATOR = (By.CSS_SELECTOR, '#typeAheadFlyOut a:not(.categories)')
    CART_BUTTON = (By.CSS_SELECTOR, '#headerCart')

    def open_p(self):
        self.open_page('https://www.homedepot.com')

    def search_product_noclick(self, text: str):
        self.input(text, *self.SEARCH_BOX_LOCATOR)

    def search_field_click(self):
        self.click(*self.SEARCH_BOX_LOCATOR)

    def search_button_click(self):
        self.click(*self.SEARCH_BUTTON_LOCATOR)

    def account_button_click(self):
        self.click(*self.ACCOUNT_BUTTON_LOCATOR)

    def register_button_click(self):
        self.wait_for_element_click(self.REGISTER_BUTTON_LOCATOR)
        self.click(*self.REGISTER_BUTTON_LOCATOR)

    def sign_in_button_click(self):
        self.wait_for_element_click(self.SIGN_IN_BUTTON_LOCATOR)
        self.click(*self.SIGN_IN_BUTTON_LOCATOR)

    def cart_button_click(self):
        self.wait_for_element_click(self.CART_BUTTON)
        self.click(*self.CART_BUTTON)

    def counting_result(self, text: str):
        self.wait_for_element_appear(self.SUGGESTIONS_CONTAINER)
        self.count_suggestion_items(text, *self.SUGGESTIONS_LOCATOR)
