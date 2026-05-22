from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage:

    FORGOT_LOGIN_LINK = (By.LINK_TEXT, "Forgot login info?")

    FIRST_NAME = (By.ID, "firstName")

    LAST_NAME = (By.ID, "lastName")

    ADDRESS = (By.ID, "address.street")

    CITY = (By.ID, "address.city")

    STATE = (By.ID, "address.state")

    ZIPCODE = (By.ID, "address.zipCode")

    SSN = (By.ID, "ssn")

    FIND_LOGIN_BUTTON = (By.XPATH, "//input[@value='Find My Login Info']")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_forgot_login_link(self):

        forgot_link = self.wait.until(
            EC.element_to_be_clickable(self.FORGOT_LOGIN_LINK)
        )

        forgot_link.click()

    def enter_recovery_details(self):

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys("Ram")

        self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        ).send_keys("Bandaru")

        self.wait.until(
            EC.visibility_of_element_located(self.ADDRESS)
        ).send_keys("Vijayawada")

        self.wait.until(
            EC.visibility_of_element_located(self.CITY)
        ).send_keys("Vijayawada")

        self.wait.until(
            EC.visibility_of_element_located(self.STATE)
        ).send_keys("Andhra Pradesh")

        self.wait.until(
            EC.visibility_of_element_located(self.ZIPCODE)
        ).send_keys("520001")

        self.wait.until(
            EC.visibility_of_element_located(self.SSN)
        ).send_keys("123456")

    def click_find_login_button(self):

        find_button = self.wait.until(
            EC.element_to_be_clickable(self.FIND_LOGIN_BUTTON)
        )

        find_button.click()