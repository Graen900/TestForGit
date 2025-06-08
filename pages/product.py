import time

from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        title_on = self.browser.find_element(By.XPATH, '//h2')
        assert title_on.text == title
