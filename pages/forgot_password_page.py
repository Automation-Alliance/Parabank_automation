from selenium.webdriver.common.by import By


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

    def click_forgot_login_link(self):
        self.driver.find_element(*self.FORGOT_LOGIN_LINK).click()

    def enter_recovery_details(self):

        self.driver.find_element(*self.FIRST_NAME).send_keys("Ram")
        self.driver.find_element(*self.LAST_NAME).send_keys("Bandaru")
        self.driver.find_element(*self.ADDRESS).send_keys("Vijayawada")
        self.driver.find_element(*self.CITY).send_keys("Vijayawada")
        self.driver.find_element(*self.STATE).send_keys("Andhra Pradesh")
        self.driver.find_element(*self.ZIPCODE).send_keys("520001")
        self.driver.find_element(*self.SSN).send_keys("123456")

    def click_find_login_button(self):
        self.driver.find_element(*self.FIND_LOGIN_BUTTON).click()