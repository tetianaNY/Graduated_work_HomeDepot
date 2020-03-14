from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class ResultsPage(Page):
    ORIGINAL_KEYWORD_H1 = (By.CSS_SELECTOR, "h1 .original-keyword")
    REVIEW_BUTTON = (By.CSS_SELECTOR, '.write-review-content__submit__desktop__button .bttn__content')
    FIRST_SEARCH_ITEM = (By.CSS_SELECTOR, '.js-pod')
    EXPECTED_ITEM_IN_THE_CART = (By.CSS_SELECTOR, '#headerCart .MyCart__itemCount')
    SECOND_PAGE_SEARCH_RESULT_LINK = (By.CSS_SELECTOR, '.grid .hd-pagination__link[title="2"]')

    def verify_header_result(self, text):
        self.wait_for_element_appear(self.ORIGINAL_KEYWORD_H1)
        self.verify_elmnt_txt(text, *self.ORIGINAL_KEYWORD_H1)

    def first_search_result_open(self):
        self.wait_for_element_click(self.FIRST_SEARCH_ITEM)
        self.click(*self.FIRST_SEARCH_ITEM)

    def review_button_check(self):
        self.wait_for_element_appear(self.REVIEW_BUTTON)
        self.verify_text_in('Write a review', *self.REVIEW_BUTTON)

    def second_page_first_search_result_open(self):
        self.wait_for_element_click(self.SECOND_PAGE_SEARCH_RESULT_LINK)
        self.click(*self.SECOND_PAGE_SEARCH_RESULT_LINK)
        self.wait_for_element_click(self.FIRST_SEARCH_ITEM)
        self.click(*self.FIRST_SEARCH_ITEM)

    def click_cart_button(self):
        self.wait_for_element_appear(self.EXPECTED_ITEM_IN_THE_CART)
        self.click(*self.EXPECTED_ITEM_IN_THE_CART)
