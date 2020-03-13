from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class ShoppingCart(Page):
    EMPTY_CART_RESULT = (By.CSS_SELECTOR, '[data-automation-id="appEmptyShoppingCartText"]')
    ADD_TO_CART_FOR_DELIVERY = (By.CSS_SELECTOR, 'div.buybelt__online-wrapper span.bttn__content')
    POPUP_ROOT = (By.CSS_SELECTOR, '#root')
    EXPECTED_ITEM_IN_THE_CART = (By.CSS_SELECTOR, '#headerCart .MyCart__itemCount')
    IFRAME_CLICKABLE_CART_ITEM = (By.CSS_SELECTOR, '[data-automation-id="viewCartLink"]')
    IFRAME_WITH_ITEM_IN_CART = (By.CSS_SELECTOR, '[data-automation-id="closeAddToCartOverlay"]')
    BOTTOM_POPUP = (By.ID, 'LPMcloseButton')
    IFRAME_LOCATOR = (By.CSS_SELECTOR, 'iframe.thd-overlay-frame')
    CART_QUANTITY = (By.CSS_SELECTOR, '[data-automation-id="itemQuantityBoxQuantityInput"]')
    ANY_PLACE_CLICK_CART = (By.CSS_SELECTOR, '[data-automation-id="itemTotalPrice"]')

    def empty_cart_result(self, text: str):
        self.wait_for_element_appear(self.EMPTY_CART_RESULT)
        self.verify_text_in(text, *self.EMPTY_CART_RESULT)

    def add_to_cart_for_delivery(self):
        self.wait_for_element_appear(self.ADD_TO_CART_FOR_DELIVERY)
        if len(self.find_elements(*self.BOTTOM_POPUP)) > 0:
            self.click(*self.BOTTOM_POPUP)
        self.click(*self.ADD_TO_CART_FOR_DELIVERY)
        self.wait_for_element_appear(self.IFRAME_LOCATOR)

    def item_in_the_cart_result(self, text: str):
        sleep(6)
        # frame = self.find_element(self.IFRAME_LOCATOR)
        # self.driver.switch_to_frame(frame)
        # self.click(*self.IFRAME_WITH_ITEM_IN_ART)
        # print(self.driver.window_handles)
        # self.wait_for_element_click(self.IFRAME_WITH_ITEM_IN_CART)
        # self.wait_for_element_appear(self.IFRAME_WITH_ITEM_IN_CART)
        self.verify_text_in(text, *self.EXPECTED_ITEM_IN_THE_CART)

    def twice_browser_back(self):
        sleep(6)
        self.back()
        self.back()

    def change_quantity(self, quantity: str):
        self.wait_for_element_appear(self.CART_QUANTITY)
        self.input(quantity, *self.CART_QUANTITY)
        self.click(*self.ANY_PLACE_CLICK_CART)
