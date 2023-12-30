from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        add_to_cart_button = self.find_element(*self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
