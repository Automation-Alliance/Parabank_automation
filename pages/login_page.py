from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//input[@value='Log In']")

    def enter_username(self, username):
        self.enter_text(self.username, username)

    def enter_password(self, password):
        self.enter_text(self.password, password)

    def click_login(self):
        self.click_element(self.login_button)

    def login_to_application(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()