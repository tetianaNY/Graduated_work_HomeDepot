from pages.main_page import MainPage
from pages.results_page import ResultsPage
from pages.registration_page import Registration
from pages.shopping_cart import ShoppingCart

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.registration_page = Registration(self.driver)
        self.shopping_cart = ShoppingCart(self.driver)


