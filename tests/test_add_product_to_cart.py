from selenium.webdriver.edge.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest
from utilities.input_data  import USERNAME, PASSWORD, PRODUCT_NAME


@pytest.mark.usefixtures("browser")
class TestAmazon:
    
    def test_login(self, browser: WebDriver):
        login_page = LoginPage(browser)
        login_page.open(login_page.base_url)
        login_page.login(USERNAME, PASSWORD)

    def test_add_to_cart(self, browser: WebDriver):
        home_page = HomePage(browser)
        home_page.search_for_product(PRODUCT_NAME)
        home_page.select_product()
        prod_page = ProductPage(browser)
        prod_page.add_to_cart()
        cart_page = CartPage(browser)
        cart_page.go_to_cart()
        txt = cart_page.verify_cart()
        a= txt[0:12]
        assert "Apple iPhone" == a




        
        
       