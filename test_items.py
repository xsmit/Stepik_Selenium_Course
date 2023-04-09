from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# запуск: pytest --language=es test_items.py


def test_check_if_btn_add_to_cart_is_present(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > ubutton")
    except NoSuchElementException:
        assert False, "Button 'Add to cart' does not exist"
