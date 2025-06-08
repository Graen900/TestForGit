import time
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_c6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")

# def test_monitors(browser):
#     browser.get("https://demoblaze.com/")
#     monitors = browser.find_element(By.XPATH, '//a[text()="Monitors"]')
#     monitors.click()
#     time.sleep(1)
#     two_monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
#     assert len(two_monitors) == 2
