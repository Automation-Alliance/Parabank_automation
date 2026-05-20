from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (By.NAME, "username")

    PASSWORD = (By.NAME, "password")

    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):

        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text.strip()
