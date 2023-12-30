from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "ap_email")
    PASSWORD_FIELD = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    login_btn = (By.XPATH,"//span[text()='Hello, sign in']")
    continue_btn = (By.ID,"continue")
    # sign_out_btn = (By.XPATH,'//span[@class="Sign Out"]')
    ALL_BTN = (By.XPATH,"//a[@id='nav-hamburger-menu']")
    SIGNOUT_BTN = (By.XPATH,"//a[text()='Sign Out']")

    def login(self, username, password):
        log_in = self.find_element(*self.login_btn)
        log_in.click()
        self.login_code(username,password)

    def login_code(self,username,password):
        username_field = self.find_element(*self.USERNAME_FIELD)
        username_field.send_keys(username)
        cont_btn = self.find_element(*self.continue_btn)
        cont_btn.click()
        password_field = self.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)
        sign_in_button = self.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.click()

    def signout(self):
        all_options = self.find_element(*self.ALL_BTN)
        all_options.click()
        sign_out = self.find_element(*self.SIGNOUT_BTN)
        sign_out.click()

    def relogin(self,username,password):
        self.login_code(username,password)