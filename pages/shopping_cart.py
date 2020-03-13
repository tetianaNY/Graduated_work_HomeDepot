from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class ShoppingCart(Page):

    EMPTY_CART_RESULT = (By.CSS_SELECTOR, '[data-automation-id="appEmptyShoppingCartText"]')

    def empty_cart_result(self, text: str):
        self.wait_for_element_appear(self.EMPTY_CART_RESULT)
        self.verify_text_in(text, *self.EMPTY_CART_RESULT)
