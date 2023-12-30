from .base_page import BasePage
from selenium.webdriver.common.by import By
class CartPage(BasePage):
    GOTO_CART = (By.XPATH,"//a[@href='/cart?ref_=sw_gtc']")
    CART_TEXT = (By.XPATH,"//span[@class='a-truncate-cut']")
    DELETE_BTN = (By.XPATH,"//input[@value='Delete']")
    CART_ICON = (By.ID,"nav-cart")
    CHECK_CART = (By.XPATH,"//h1[contains(text(),'Your Amazon Cart is empty.')]")

    def go_to_cart(self):
        go_to_cart_btn = self.find_element(*self.GOTO_CART)
        go_to_cart_btn.click()

    def verify_cart(self):
        Prod_name = self.find_element(*self.CART_TEXT)
        return Prod_name.text
    
    def remove_product(self):
        dlt_btn = self.find_element(*self.DELETE_BTN)
        dlt_btn.click()
    
    def cart_icon_click(self):
        cart = self.find_element(*self.CART_ICON)   
        cart.click()
        # raw_txt = self.find_element(*self.CHECK_CART)
        # return raw_txt.text

    def get_cart_items(self):
        raw_txt = self.find_element(*self.CHECK_CART)
        return raw_txt.text 