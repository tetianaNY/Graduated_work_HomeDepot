from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)
        self.alerts = Alert(self.driver)

    def open_page(self, url: str):
        self.driver.get(url)

    def input(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def back(self):
        self.driver.back()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def hover_over_element(self, *locator):
        elem = self.find_element(*locator)
        self.actions.move_to_element(elem).perform()

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(*locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(*locator))

    def wait_for_element_click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(*locator))

    def wait_for_element_located(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_until_alert_is_present(self):
        return self.driver.wait.until(EC.alert_is_present())

    def verify_text_in(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        # print(actual_text)
        assert expected_text in actual_text, f'Expected text {expected_text}, not in {actual_text}'

    def verify_elmnt_txt(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def count_suggestion_items(self, text: str, *locator):
        total = str(len(self.driver.find_elements(*locator))-1)
        print(f'Total suggestions for "{text}" is: {total}.')

