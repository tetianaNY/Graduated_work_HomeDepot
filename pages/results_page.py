from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ResultsPage(Page):
    ORIGINAL_KEYWORD_H1 = (By.CSS_SELECTOR, "h1 .original-keyword")

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





















