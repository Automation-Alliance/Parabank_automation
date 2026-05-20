from selenium.webdriver.common.by import By


class LoginPage:

    USERNAME = (By.NAME, "username")

    PASSWORD = (By.NAME, "password")

    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")

    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'The username and password could not be verified')]",
    )

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):

        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):

        return self.driver.find_element(*self.ERROR_MESSAGE).text
