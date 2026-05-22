from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (
        By.NAME,
        "username"
    )

    PASSWORD = (
        By.NAME,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//input[@value='Log In']"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "p.error"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    def enter_username(self, username):

        username_field = self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        )

        username_field.send_keys(
            username
        )

    def enter_password(self, password):

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        password_field.send_keys(
            password
        )

    def click_login_button(self):

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        login_button.click()

    def get_error_message(self):

        error_element = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return error_element.text.strip()