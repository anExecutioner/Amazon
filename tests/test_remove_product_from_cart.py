from selenium.webdriver.edge.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest
from utilities.input_data  import USERNAME, PASSWORD, PRODUCT_NAME
from selenium.webdriver.common.action_chains import ActionChains
import time
@pytest.mark.usefixtures("browser")   
class TestEmptyCart:

    def test_sign_out(self, browser: WebDriver):
        time.sleep(5)
        login_page = LoginPage(browser)
        login_page.signout()

    def test_relogin(self,browser: WebDriver):
        login_page = LoginPage(browser)
        login_page.relogin(USERNAME,PASSWORD)

    def test_remove_items_from_cart(self,browser):
        cart_page = CartPage(browser)
        cart_page.cart_icon_click()
        cart_page.remove_product()
        txt = cart_page.get_cart_items()
        assert 'Your Amazon Cart is empty.' == txt

    