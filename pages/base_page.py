from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def input(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def back(self):
        self.driver.back()

    def wait_for_element_click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(*locator))


    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_elmnt_txt(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def count_suggestion_items(self, text: str, *locator):
        total = str(len(self.driver.find_elements(*locator))-1)
        print(f'Total suggestions for "{text}" is: {total}.')

    def verify_text_in(self, text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        print(actual_text)
        assert text in actual_text, f'Operation was not successful'

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(*locator))





