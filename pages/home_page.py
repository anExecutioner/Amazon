from .base_page import BasePage
from selenium.webdriver.common.by import By
class HomePage(BasePage):
    
    SEARCH_BAR = (By.ID,"twotabsearchtextbox")
    SEARCH_ICON = (By.ID,"nav-search-submit-button")
    PROD_SELECTION = (By.XPATH,"//div[@class='aok-relative']")

    
    def search_for_product(self,product):
        search_bar = self.find_element(*self.SEARCH_BAR)
        search_bar.send_keys(product)

        search_icon= self.find_element(*self.SEARCH_ICON)
        search_icon.click()
        # self.act("ENTER")
    
    def select_product(self):
        prod_select = self.find_element(*self.PROD_SELECTION)
        prod_select.click()










